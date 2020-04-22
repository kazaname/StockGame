from django import forms
from .models import Wallet
from stockgame.vulgarity_list import (vulgarity_pl,
                                      vulgarity_english,
                                      vulgarity_spain,
                                      vulgarity_italy,
                                      vulgarity_indonesia,
                                      vulgarity_france)

class WalletModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                         "placeholder": "Twoja nazwa portfela",
                                                         "required": True}))
    minimum_commission = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                         "placeholder": "Minimalna prowizja",
                                                         "required": True}))
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
        qs = Wallet.objects.filter(name__iexact=name)
        if qs.exists():
            raise forms.ValidationError("Portfel o nazwie {name} już stworzyłeś. "
                                        "Proszę wybrać inną nazwę dla swojego portfela.".format(name=name))
        elif len(name) < 5:
            raise forms.ValidationError("Nazwa portfela musi zawierać conajmniej 5 znaków. Proszę zmień nazwę.")
        elif name.lower() in vulgarity_pl:
            raise forms.ValidationError("Wulgaryzmom mówimy stanowcze CHYBA NIE ;). Proszę zmień nazwę.")
        elif name.lower() in vulgarity_english:
            raise forms.ValidationError("Sorry but english wulgaryzmy też są prohibited :). Proszę zmień nazwę.")
        elif name.lower() in vulgarity_spain:
            raise forms.ValidationError("Godne podziwu, że znasz Hiszpański, ale to też nie przejdzie :O. Proszę zmień nazwę.")
        elif name.lower() in vulgarity_italy:
            raise forms.ValidationError("Cóż mogę żec 'non passerà' :P. Proszę zmień nazwę.")
        elif name.lower() in vulgarity_france:
            raise forms.ValidationError("Zdradzę Ci tajemnicę Francuskie wulgaryzmy też nie przejdą :D. Proszę zmień nazwę.")
        elif name.lower() in vulgarity_indonesia:
            raise forms.ValidationError("Tak nawet w języku Indonezyjskim sprawdzamy wulgaryzmy ;D. Proszę zmień nazwę.")
        return name



class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control",
                                                             "placeholder": "Your full name"}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control",
                                                           "placeholder": "Your message"}))