from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() !='z':
        raise forms.ValidationError("Name needs to start with Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email= forms.EmailField()
    very_email=forms.EmailField(label="Mail Again:")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    """
    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("GOTCHA BOT")
        return botcatcher
"""
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail= all_clean_data['very_email']
        if(email!=vmail):
            raise.forms.ValidationError("Email doesnt matches")
