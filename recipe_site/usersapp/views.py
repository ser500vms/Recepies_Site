from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView, 
    CreateView,
    DeleteView,
    UpdateView,
    ListView
)
from .form import CustomUserForm
from django.contrib.auth.views import (
LoginView, 
LogoutView, 
PasswordChangeView,
PasswordResetDoneView, 
PasswordResetView,
PasswordResetConfirmView,
PasswordResetCompleteView,
)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
)
from recipiesapp.models import Recipe, Category
from django.db.models import Q


# Create your views here.


class HomeView(ListView):
    template_name = "base.html"
    paginate_by = 3
    model = Recipe
    context_object_name = "recipies"
    
    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        categories  = self.request.GET.getlist('categories')  # Получаем выбранные категории

        queryset = Recipe.objects.all()

        # Если есть запрос по названию
        if query:
            queryset = queryset.filter(Q(name__icontains=query.lower()) | Q(name__icontains=query.capitalize()))

        # Если есть выбранные категории
        if categories:
            queryset = queryset.filter(categories__id__in=categories).distinct()

        # Получаем количество отображаемых рецептов из GET параметров
        # count = self.request.GET.get('count', self.paginate_by)

        return  queryset # Возвращаем уникальные рецепты
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context


class AboutUserView(LoginRequiredMixin, TemplateView):
    template_name = "pages/about-user.html"
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context


class LkView(LoginRequiredMixin, ListView):
    template_name = "pages/account-page.html"
    paginate_by = 3
    model = Recipe
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    context_object_name = "recipies"


    def get_queryset(self):
        # Фильтруем рецепты по текущему пользователю
        return Recipe.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context
    

class RegistrationView(CreateView):
    form_class = CustomUserForm
    template_name = "pages/registration.html"

    def form_valid(self, form):
        response = super().form_valid(form)


        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)

        return response
    
    def get_success_url(self):
        return reverse_lazy('lk_page', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context
    

class MyLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "pages/enter-page.html"
    
    
    def get_success_url(self):
        return reverse_lazy('lk_page', kwargs={'pk': self.request.user.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context
    

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context

 
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView, UserPassesTestMixin):
    form_class = PasswordChangeForm
    template_name = 'pages/user_password_change_form.html'
    success_url = reverse_lazy('user_info')  # перенаправление после успешного изменения пароля

    def get_success_url(self):
        return reverse_lazy('user_info', kwargs={'pk': self.request.user.pk})
    
    def get_object(self, queryset=None):
    # Возвращаем текущего пользователя
        return self.request.user  
    
    def test_func(self):
    # Позволяем редактировать только собствен данные        
        return self.request.user == self.get_object()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context
    
    
class UserPasswordResetView(PasswordResetView):
        template_name = 'pages/password_reset_form.html'
        email_template_name = 'pages/password_reset_email.html'
        success_url = reverse_lazy("password_reset_done")

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['categories'] = Category.objects.all()  # Передаем все категории в контекст
            return context


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'pages/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context
    

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'pages/password_reset_confirm.html'
    success_url = reverse_lazy("password_reset_complete")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context
    

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name='pages/password_reset_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаем все категории в контекст
        return context