from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RecipeForm
from .models import Recipe
from django.views.generic import (
    TemplateView, 
    CreateView,
    DeleteView,
    UpdateView,
)
from .forms import RecipeForm


class AddRecipeView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = "recipiesapp/add-recipe.html"

    def get_success_url(self):
        return reverse(
            "recipe",
            kwargs={"pk": self.object.pk},
        )

    def form_valid(self, form):
        # Устанавливаем автора как текущего пользователя
        form.instance.author = self.request.user
        return super().form_valid(form)  

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Убираем предзаполнение данных при GET-запросе
        if self.request.method == 'GET':
            kwargs.update({'instance': None})
        return kwargs  
    

class RecipeView(TemplateView):
    template_name = "recipiesapp/recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')  # Получаем pk из URL
        context['recipe'] = get_object_or_404(Recipe, pk=pk)  # Получаем рецепт по pk
        return context


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recipe
    template_name = "pages/confirm-delete.html"
    success_url = reverse_lazy("home_page")
    
    def test_func(self):
    # Позволяем редактировать только собствен данные        
        return self.request.user == self.get_object().author


class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recipe
    fields = "name", "short_description", "categories", "image", "cooking_time", "quantity_of_servings", "ingridients", "cooking_steps"
    template_name = "recipiesapp/recipe_update_form.html"

    def form_valid(self, form):
        # Устанавливаем автора как текущего пользователя
        form.instance.author = self.request.user
        return super().form_valid(form)  
    
    def test_func(self):
    # Позволяем редактировать только собствен данные        
        return self.request.user == self.get_object().author
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем список ID выбранных категорий для текущего рецепта
        context['selected_categories'] = self.object.categories.values_list('id', flat=True)
        return context

    def get_success_url(self):
        return reverse(
            "recipe",
            kwargs={"pk": self.object.pk},
        )