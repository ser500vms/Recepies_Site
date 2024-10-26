from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .form import CustomUserForm


# Create your views here.


class HomeView(TemplateView):
    template_name = "base.html"


# class RegistrationView(TemplateView):
#     template_name = "pages/registration.html"


class RegistrationView(CreateView):
    form_class = CustomUserForm
    template_name = "pages/registration.html"
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        response = super().form_valid(form)
        User.objects.create(user=self.object)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)

        return response
