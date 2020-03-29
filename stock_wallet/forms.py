from django import forms
from .models import Wallet

class WalletModelForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = [
            'name',
            'cash',
            'minimum_commission',
            'percentage_commission',
            'is_private',
            'comment',
        ]


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "Your full name"}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                           "placeholder": "Your message"}))