from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.views.generic import ListView, DetailView, View

from .forms import UserSignUpForm
from .tokens import account_activation_token


class UserSignUpView(View):
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        title = 'Utwórz konto'
        form = UserSignUpForm()
        context = {"title": title, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Aktywuj swoje konto investora.'
            message = render_to_string('account/account_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            new_user_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[new_user_email])
            email.send()
            messages.success(request, 'Twoje konto zostało utworzone. Aktywuj je klikając w link przesłany w wiadomości e-mail.')
            return redirect('home')

        title = 'Utwórz konto'
        context = {"title": title, 'form': form}
        return render(request, self.template_name, context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        # return render(request, '')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# def signup_view(request):
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('home')
#     return render(request, 'signup.html', {'form': form})