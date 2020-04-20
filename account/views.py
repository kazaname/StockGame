from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View

from .forms import RegisterForm

class Register(View):
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        title = 'Utwórz konto'
        form = RegisterForm()
        context = {"title": title, 'form': form}
        return render(request, self.template_name, context)