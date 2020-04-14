from django import forms
from .models import Wallet
from .vulgarity_pl_list import vulgarity_pl


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

    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        qs = Wallet.objects.filter(name=name)
        if qs.exists():
            raise forms.ValidationError("Portfel o nazwie {name} już stworzyłeś. "
                                        "Proszę wybrać inną nazwę dla swojego portfela.".format(name=name))
        return name



class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "Your full name"}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                           "placeholder": "Your message"}))