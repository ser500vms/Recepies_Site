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
    extra=1,  # Количество пустых форм для добавления ингредиентов по умолчанию
    can_delete=True  # Позволяет удалять ингредиенты
)


class AddRecipeView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = "recipiesapp/add-recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Используем только одну пустую форму для начала
        context['ingredient_formset'] = RecipeIngredientFormSet(queryset=RecipeIngredient.objects.none())
        return context

    def form_valid(self, form):
        # Сохраняем рецепт
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        # Привязываем и сохраняем категории рецепта
        categories = form.cleaned_data.get('categories')
        if categories:
            self.object.categories.set(categories)


        # Создаем и сохраняем формы ингредиентов
        ingredient_formset = RecipeIngredientFormSet(self.request.POST, instance=self.object)
        if ingredient_formset.is_valid():
            ingredient_formset.save()
            return redirect(reverse("recipe", kwargs={"pk": self.object.pk}))
        else:
            return self.render_to_response(
                self.get_context_data(form=form, ingredient_formset=ingredient_formset)
            )

    def form_invalid(self, form):
        # Если форма рецепта не валидна, возвращаем ошибочный контекст
        ingredient_formset = RecipeIngredientFormSet(self.request.POST)
        return self.render_to_response(
            self.get_context_data(form=form, ingredient_formset=ingredient_formset)
        )
      

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
    fields = ["name", "short_description", "categories", "image", "cooking_time", "quantity_of_servings", "cooking_steps"]
    template_name = "recipiesapp/recipe_update_form.html"

    def form_valid(self, form):
        # Сохраняем рецепт
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        # Инициализируем формсет ингредиентов
        ingredient_formset = RecipeIngredientFormSet(self.request.POST, instance=self.object)

        # Проверка валидности формсета ингредиентов
        if ingredient_formset.is_valid():
            # Проверяем наличие id для существующих объектов
            for ingredient_form in ingredient_formset:
                if not ingredient_form.cleaned_data.get("id") and ingredient_form.instance.pk:
                    ingredient_form.cleaned_data["id"] = ingredient_form.instance.pk

            # Сохранение формсета после валидации и добавления id
            ingredient_formset.save()

            # Сохраняем выбранные категории
            form.cleaned_data['categories'] = form.cleaned_data.get('categories')
            self.object.categories.set(form.cleaned_data['categories'])

            return redirect(reverse("recipe", kwargs={"pk": self.object.pk}))
        else:
            # Логирование ошибок для отладки
            print("Ошибки formset:")
            for i, f in enumerate(ingredient_formset.forms):
                print(f"Форма ингредиента {i}: ошибки: {f.errors}")
                if 'id' in f.errors:
                    print(f"Поле 'id' формы ингредиента {i}: значение = {f['id'].value()}")

            return self.render_to_response(
                self.get_context_data(form=form, ingredient_formset=ingredient_formset)
            )


    def test_func(self):
        # Ограничение доступа только для автора рецепта
        return self.request.user == self.get_object().author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient_formset'] = RecipeIngredientFormSet(instance=self.object)  # Подключаем formset ингредиентов
        context['selected_categories'] = self.object.categories.values_list('id', flat=True)
        return context

    def form_invalid(self, form):
        # Возвращаем контекст с ошибками, если основная форма рецепта не валидна
        ingredient_formset = RecipeIngredientFormSet(self.request.POST)
        return self.render_to_response(
            self.get_context_data(form=form, ingredient_formset=ingredient_formset)
        )
    
