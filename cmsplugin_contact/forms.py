from django import forms
#import settings
from stopspam.forms import HoneyPotForm, RecaptchaForm, AkismetForm
  
class HoneyPotContactForm(HoneyPotForm):
    ABB_CHOICES = (('Dhr', 'Dhr',), ('Mevr', 'Mevr',))
    initials = forms.CharField()
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
    initials = forms.CharField()
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
    initials = forms.CharField()
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