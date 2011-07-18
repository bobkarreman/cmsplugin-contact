from django import forms
#import settings
from django.utils.translation import ugettext_lazy as _
from stopspam.forms import HoneyPotForm, RecaptchaForm, AkismetForm
from models import Contact
from stopspam.forms.widgets import RecaptchaResponse
  
class HoneyPotContactForm(HoneyPotForm):
    ABB_CHOICES = (('Mr', _('Mr'),), ('Ms', _('Ms'),))
    firstname = forms.CharField()
    lastname = forms.CharField()
    abbreviation = forms.ChoiceField(widget=forms.RadioSelect, choices=ABB_CHOICES)
    company = forms.CharField(required=False)
    function = forms.CharField(required=False)
    address = forms.CharField(required=False)
    zipcode = forms.CharField(required=False)
    city = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    mobile_phone = forms.CharField(required=False)
    
    email 	= forms.EmailField()
    website     = forms.URLField(verify_exists=False, required=False)

    # subject    = forms.CharField(required=False)
    # content    = forms.CharField(widget=forms.Textarea())
    # email     = forms.EmailField()
    # subject   = forms.CharField(required=False)
    # content   = forms.CharField(widget=forms.Textarea())


class AkismetContactForm(AkismetForm):
    akismet_fields = {
        'comment_author_email': 'email',
        # 'comment_content': 'content'
    }
    ABB_CHOICES = (('Dhr', 'Dhr',), ('Mevr', 'Mevr',))
    firstname = forms.CharField()
    lastname = forms.CharField()
    abbreviation = forms.ChoiceField(widget=forms.RadioSelect, choices=ABB_CHOICES)
    company = forms.CharField(required=False)
    function = forms.CharField(required=False)
    address = forms.CharField(required=False)
    zipcode = forms.CharField(required=False)
    city = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    mobile_phone = forms.CharField(required=False)
    
    email     = forms.EmailField()
    website     = forms.URLField(verify_exists=False, required=False)

    # subject    = forms.CharField(required=False)
    # content    = forms.CharField(widget=forms.Textarea())
    # email     = forms.EmailField()
    # subject    = forms.CharField(required=False)
    # content    = forms.CharField(widget=forms.Textarea())
    
    akismet_api_key = None
    

        
class RecaptchaContactForm(RecaptchaForm):
    ABB_CHOICES = (('Dhr', 'Dhr',), ('Mevr', 'Mevr',))
    firstname = forms.CharField()
    lastname = forms.CharField()
    abbreviation = forms.ChoiceField(widget=forms.RadioSelect, choices=ABB_CHOICES)
    company = forms.CharField(required=False)
    function = forms.CharField(required=False)
    address = forms.CharField(required=False)
    zipcode = forms.CharField(required=False)
    city = forms.CharField(required=False)
    phone = forms.CharField(required=False)
    mobile_phone = forms.CharField(required=False)
    
    email     = forms.EmailField()
    website     = forms.URLField(verify_exists=False, required=False)
    # subject    = forms.CharField(required=False)
    # content    = forms.CharField(widget=forms.Textarea())

    recaptcha_public_key = None
    recaptcha_private_key = None
    recaptcha_theme = None

    recaptcha_response_field = forms.CharField(
                widget = RecaptchaResponse,
                label = _('Please enter the two words on the image separated by a space:'),
                error_messages = {
                    'required': _('You did not enter any of the words.')
            })

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super(RecaptchaContactForm, self).__init__(*args, **kwargs)
        self.fields["firstname"].required = instance.required_firstname
        self.fields["lastname"].required = instance.required_lastname
        self.fields["abbreviation"].required = instance.required_abbreviation
        self.fields["company"].required = instance.required_company
        self.fields["function"].required = instance.required_function
        self.fields["address"].required = instance.required_address
        self.fields["zipcode"].required = instance.required_zipcode
        self.fields["city"].required = instance.required_city
        self.fields["phone"].required = instance.required_phone
        self.fields["mobile_phone"].required = instance.required_mobile_phone
        self.fields["email"].required = instance.required_email
        self.fields["website"].required = instance.required_website
