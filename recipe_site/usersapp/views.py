from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView, 
    CreateView,
    DeleteView,
    UpdateView
)
from .form import CustomUserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    PermissionRequiredMixin,
    UserPassesTestMixin
)


# Create your views here.


class HomeView(TemplateView):
    template_name = "base.html"


class AboutUserView(LoginRequiredMixin, TemplateView):
    template_name = "pages/about-user.html"
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class LkView(LoginRequiredMixin, TemplateView):
    template_name = "pages/account-page.html"
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class RegistrationView(CreateView):
    form_class = CustomUserForm
    template_name = "pages/registration.html"
    success_url = reverse_lazy("lk_page")

    def form_valid(self, form):
        response = super().form_valid(form)
        # User.objects.create(user=self.object)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)

        return response


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "pages/enter-page.html"
    
    def get_success_url(self):
        return reverse_lazy('lk_page') 
    

class MyLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("home_page")
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = "pages/confirm-delete.html"
    success_url = reverse_lazy("home_page")

    def get_object(self, queryset=None):
    # Возвращаем текущего пользователя
        return self.request.user    
    def test_func(self):
    # Позволяем редактировать только собствен данные        
        return self.request.user == self.get_object()

 

class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = "first_name", "last_name", "username", "email"
    template_name = "pages/user_update_form.html"

    def get_success_url(self):
        return reverse(
            "user_info",
            kwargs={"pk": self.object.pk},
        )
    
    def get_object(self, queryset=None):
    # Возвращаем текущего пользователя
        return self.request.user    
    def test_func(self):
    # Позволяем редактировать только собствен данные        
        return self.request.user == self.get_object()
