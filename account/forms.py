from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from stockgame.vulgarity_list import (vulgarity_pl,
                                      vulgarity_english,
                                      vulgarity_spain,
                                      vulgarity_italy,
                                      vulgarity_indonesia,
                                      vulgarity_france)


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ['username' , 'email', 'password1', 'password2']

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Nazwa użytkownika {name} jest już zajęta! "
                                        "Wybierz inną i spróbuj ponownie.".format(name=username))
        elif len(username) < 5:
            raise forms.ValidationError("Nazwa użytkownika musi zawierać conajmniej 5 znaków. Proszę zmień nazwę.")
        elif username.lower() in vulgarity_pl:
            raise forms.ValidationError("Wulgaryzmom mówimy stanowcze CHYBA NIE ;). Proszę zmień nazwę.")
        elif username.lower() in vulgarity_english:
            raise forms.ValidationError("Sorry but english wulgaryzmy też są prohibited :). Proszę zmień nazwę.")
        elif username.lower() in vulgarity_spain:
            raise forms.ValidationError("Godne podziwu, że znasz Hiszpański, ale to też nie przejdzie :O. Proszę zmień nazwę.")
        elif username.lower() in vulgarity_italy:
            raise forms.ValidationError("Cóż mogę żec 'non passerà' :P. Proszę zmień nazwę.")
        elif username.lower() in vulgarity_france:
            raise forms.ValidationError("Zdradzę Ci tajemnicę Francuskie wulgaryzmy też nie przejdą :D. Proszę zmień nazwę.")
        elif username.lower() in vulgarity_indonesia:
            raise forms.ValidationError("Tak nawet w języku Indonezyjskim sprawdzamy wulgaryzmy ;D. Proszę zmień nazwę.")
        return username

    def clean_password1(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 8:
            raise forms.ValidationError('To hasło jest zbyt krótkie. Hasło musi zawierać conajmnie 8 znaków. '
                                        'Popraw hasło i spróbuj ponownie.')

        return password1

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Podany email jest już przypisany do innego konta. "
                                        "Popraw email i spróbuj ponownie.")
        elif not email:
            raise forms.ValidationError('Email jest wymagany do weryfikacji konta. '
                                        'Wprowadź adres email i spróbuj ponownie.')
        return email