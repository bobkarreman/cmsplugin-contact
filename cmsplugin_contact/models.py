from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

class Contact(CMSPlugin):
    SPAM_PROTECTION_CHOICES = (
        (0, 'Honeypot'),
        (1, 'Akismet'),
        (2, 'ReCAPTCHA'),
    )
    
    THEME_CHOICES = (
        ('clean', 'Clean'),
        ('red', 'Red'),
        ('white', 'White'),
        ('blackglass', 'Black Glass'),
        ('custom', 'Custom'),
    )
    
    site_email = models.EmailField(_('Email recipient'))
    email_label = models.CharField(_('Email sender label'), default=_('Your email address'), max_length=100)
    subject_label = models.CharField(_('Subject label'), default=_('Subject'), max_length=200)
    content_label = models.CharField(_('Message content label'), default=_('Message'), max_length=100)
    thanks = models.TextField(verbose_name=_("Thanks message"), help_text=_('Message displayed on successful submit'), default=_('Thank you for your message.'), max_length=200)
    submit = models.CharField(_('Submit button value'), default=_('Submit'), max_length=30)
    
    spam_protection_method = models.SmallIntegerField(verbose_name=_('Spam protection method'), choices=SPAM_PROTECTION_CHOICES, default=0)
    
    akismet_api_key = models.CharField(max_length=255, blank=True)
    
    recaptcha_public_key = models.CharField(max_length=255, blank=True)
    recaptcha_private_key = models.CharField(max_length=255, blank=True)
    recaptcha_theme = models.CharField(max_length=20, choices=THEME_CHOICES, default='clean', verbose_name=_('ReCAPTCHA theme'))
    

    required_firstname = models.BooleanField(_('Firstname required'))
    required_lastname = models.BooleanField(_('Lastname required'))
    required_abbreviation = models.BooleanField(_('Title required'))
    required_company = models.BooleanField(_('Company required'))
    required_function = models.BooleanField(_('Function required'))
    required_address = models.BooleanField(_('Address required'))
    required_zipcode = models.BooleanField(_('Zipcode required'))
    required_city = models.BooleanField(_('City required'))
    required_phone = models.BooleanField(_('Phone required'))
    required_mobile_phone = models.BooleanField(_('Mobile required'))
    required_email = models.BooleanField(_('E-Mail required'))
    required_website = models.BooleanField(_('Website required'))

    
    def __unicode__(self):
        return self.site_email
