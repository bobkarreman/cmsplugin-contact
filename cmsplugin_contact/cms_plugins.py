from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import CharField
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.plugins.text.settings import USE_TINYMCE
from cms.plugins.text.widgets.wymeditor_widget import WYMEditor
from models import Contact
from forms import AkismetContactForm, RecaptchaContactForm, HoneyPotContactForm
from django.core.mail import EmailMessage
from admin import ContactAdminForm

class ContactPlugin(CMSPluginBase):
    model = Contact
    name = _("Contact Form")
    render_template = "cmsplugin_contact/contact.html"
    form = ContactAdminForm
    
    fieldsets = (
        (None, {
            'fields': ('site_email', 'email_label', 'subject_label', 'content_label', 'thanks', 'submit'),
        }),

        (_('Required Fields'), {
            'fields': ('required_firstname', 'required_lastname', 'required_abbreviation', 'required_company', 'required_function', 'required_address', 'required_zipcode', 'required_city', 'required_phone', 'required_mobile_phone', 'required_email', 'required_website')
        }),
        
        (_('Spam Protection'), {
            'fields': ('spam_protection_method', 'akismet_api_key', 'recaptcha_public_key', 'recaptcha_private_key', 'recaptcha_theme')
        })
    )
    
    change_form_template = "cmsplugin_contact/admin/plugin_change_form.html"

    def get_editor_widget(self, request, plugins):
        """
        Returns the Django form Widget to be used for
        the text area
        """
        if USE_TINYMCE and "tinymce" in settings.INSTALLED_APPS:
            from cms.plugins.text.widgets.tinymce_widget import TinyMCEEditor
            return TinyMCEEditor(installed_plugins=plugins)
        else:
            return WYMEditor(installed_plugins=plugins)

    def get_form_class(self, request, plugins):
        """
        Returns a subclass of Form to be used by this plugin
        """
        # We avoid mutating the Form declared above by subclassing
        class TextPluginForm(self.form):
            pass
        widget = self.get_editor_widget(request, plugins)
        TextPluginForm.declared_fields["thanks"] = CharField(widget=widget, required=False)
        return TextPluginForm


    def get_form(self, request, obj=None, **kwargs):
        plugins = plugin_pool.get_text_enabled_plugins(self.placeholder, self.page)
        form = self.get_form_class(request, plugins)
        kwargs['form'] = form # override standard form
        return super(ContactPlugin, self).get_form(request, obj, **kwargs)

    def create_form(self, instance, request):
        if instance.get_spam_protection_method_display() == 'Akismet':
            AkismetContactForm.aksimet_api_key = instance.akismet_api_key
            FormClass = AkismetContactForm
        elif instance.get_spam_protection_method_display() == 'ReCAPTCHA':
            RecaptchaContactForm.instance = instance
            RecaptchaContactForm.recaptcha_public_key = getattr(settings, "RECAPTCHA_PUBLIC_KEY", \
                                                        instance.recaptcha_public_key)
            RecaptchaContactForm.recaptcha_private_key = getattr(settings, "RECAPTCHA_PRIVATE_KEY", \
                                                         instance.recaptcha_private_key)
            RecaptchaContactForm.recaptcha_theme = instance.recaptcha_theme
            # FormClass = RecaptchaContactForm
            if request.method == "POST":
                return RecaptchaContactForm(request, instance=instance, data=request.POST)
            else:
                return RecaptchaContactForm(request, instance=instance)
                
        else:
            FormClass = HoneyPotContactForm
            
        if request.method == "POST":
            return FormClass(request, data=request.POST)
        else:
            return FormClass(request)


    def send(self, form, site_email):
        email_message = EmailMessage(
            'vcard',
            render_to_string("cmsplugin_contact/email.txt", {
                'data': form.cleaned_data,
            }),
            form.cleaned_data['email'],
            [site_email],
            headers = {
                'Reply-To': form.cleaned_data['email']
            },)

        vcard_data = render_to_string("cmsplugin_contact/vcard.txt", form.cleaned_data),

        email_message.attach('vcard.vcf', vcard_data[0], 'text/x-vcard')            
        email_message.send(fail_silently=True)
    
    def render(self, context, instance, placeholder):
        request = context['request']

        form = self.create_form(instance, request)
    
        if request.method == "POST" and form.is_valid():
            self.send(form, instance.site_email)
            context.update( {
                'contact': instance,
            })
        else:
            context.update({
                'contact': instance,
                'form': form,
            })
            
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'spam_protection_method': obj.spam_protection_method if obj else 0,
            'recaptcha_settings': hasattr(settings, "RECAPTCHA_PUBLIC_KEY"),
            'akismet_settings': hasattr(settings, "AKISMET_API_KEY"),
        })
        
        return super(ContactPlugin, self).render_change_form(request, context, add, change, form_url, obj)
        
    
plugin_pool.register_plugin(ContactPlugin)
