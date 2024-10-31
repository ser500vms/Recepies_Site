from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RecipeForm, RecipeIngredientForm
from .models import Recipe, RecipeIngredient
from django.views.generic import (
    TemplateView, 
    CreateView,
    DeleteView,
    UpdateView,
)
from .forms import RecipeForm


RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    form=RecipeIngredientForm,
    extra=2,  # Количество пустых форм для добавления ингредиентов по умолчанию
    can_delete=True  # Позволяет удалять ингредиенты
)

class AddRecipeView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = "recipiesapp/add-recipe.html"

    # def get_success_url(self):
    #     return reverse("recipe", kwargs={"pk": self.object.pk})

    def get(self, request):
        form = RecipeForm()
        ingredient_formset = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())
        return render(request, 'recipiesapp/add-recipe.html', {
            'form': form,
            'ingredient_formset': ingredient_formset,
        })

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        ingredient_formset = RecipeIngredientFormSet(request.POST)

        if form.is_valid() and ingredient_formset.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            ingredient_formset.instance = recipe
            ingredient_formset.save()

            # Используем 'recipe.pk' для перенаправления после сохранения
            return redirect(reverse("recipe", kwargs={"pk": recipe.pk}))  

        # Если формы не прошли валидацию, рендерим страницу с ошибками
        return render(request, 'recipiesapp/add-recipe.html', {
            'form': form,
            'ingredient_formset': ingredient_formset,
        })
        

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