from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProductForm, RecipeForm, RecipeIngredientForm
from .models import Category, Product, Recipe, RecipeIngredient, RecipeStep
from django.views.generic import (
    TemplateView, 
    CreateView,
    DeleteView,
    UpdateView,
)
from .forms import RecipeForm, RecipeStepForm
from decimal import Decimal, ROUND_UP
from django.db.models import Q


# для автозаполнение продуктов, обработка запроса в выпадающем списке
def product_autocomplete(request):
    query = request.GET.get('q', '')  # Получаем строку запроса, которую вводит пользователь
    products = Product.objects.filter(Q(name__icontains=query.lower()) | Q(name__icontains=query.capitalize()))[:5]  # Фильтруем продукты и ограничиваем результат до 5
    results = [{'id': product.id, 'name': product.name} for product in products]
    return JsonResponse(results, safe=False)


RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    form=RecipeIngredientForm,
    extra=1,  # Количество пустых форм для добавления ингредиентов по умолчанию
    can_delete=True  # Позволяет удалять ингредиенты
)


RecipeStepFormSet = inlineformset_factory(
    Recipe,
    RecipeStep,
    form=RecipeStepForm,
    extra=1,  # Количество пустых форм для добавления ингредиентов по умолчанию
    can_delete=True  # Позволяет удалять ингредиенты
)


class AddRecipeView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = "recipiesapp/add-recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Используем только одну пустую форму для начала
        context['ingredient_formset'] = RecipeIngredientFormSet(self.request.POST or None)
        context['step_formset'] = RecipeStepFormSet(self.request.POST or None)
        selected_categories = self.request.POST.getlist('categories') if self.request.method == 'POST' else []
        context['selected_categories'] = [int(category) for category in selected_categories]
        
        return context


    def form_valid(self, form):

        # Создаем и сохраняем формы ингредиентов
        ingredient_formset = RecipeIngredientFormSet(self.request.POST)
            
        step_formset = RecipeStepFormSet(self.request.POST)

        form_valid = form.is_valid()
        ingredient_valid = ingredient_formset.is_valid()
        step_valid = step_formset.is_valid()

        # Проверяем, что хотя бы один ингредиент заполнен
        ingredients_have_data = any(
            form.cleaned_data.get('product') for form in ingredient_formset.forms if form.cleaned_data
        )

        # Дополнительная проверка на наличие хотя бы одного заполненного шага
        steps_have_text = any(
            form.cleaned_data.get('text') for form in step_formset if form.cleaned_data
        )

        if form_valid and ingredient_valid and step_valid and ingredients_have_data and steps_have_text:
            print("Valid")
            # Сохраняем рецепт
            self.object = form.save(commit=False)
            self.object.author = self.request.user
            self.object.save()



            # Привязываем и сохраняем категории рецепта
            categories = form.cleaned_data.get('categories')
            if categories:
                self.object.categories.set(categories)


            ingredient_formset.instance = self.object
            ingredient_formset.save()

            step_formset.instance = self.object
            step_formset.save()


            # Подсчет калорий для рецепта
            total_calories = 0
            total_fats = 0
            total_carbohydrates = 0
            total_proteins = 0
            for ingredient_form in ingredient_formset:
                # Проверка, что product и quantity присутствуют в cleaned_data
                if 'product' in ingredient_form.cleaned_data and 'quantity' in ingredient_form.cleaned_data:
                    unit_of_measurement = ingredient_form.cleaned_data['unit_of_measurement']

                    match unit_of_measurement:
                        case 'Ч.л':
                            quantity = Decimal(ingredient_form.cleaned_data['quantity'] * 5)
                        case 'С.л':
                            quantity = Decimal(ingredient_form.cleaned_data['quantity'] * 15)
                        case 'По вкусу':
                            quantity = 0
                        case _:
                            quantity = Decimal(ingredient_form.cleaned_data['quantity'])
                    
                    product = ingredient_form.cleaned_data['product']
                    unit_calories = Decimal(product.calories / 100)  # калорийность продукта на единицу измерения
                    unit_fats = Decimal(product.fats / 100)
                    unit_carbohydrates = Decimal(product.carbohydrates / 100)
                    unit_proteins = Decimal(product.proteins / 100)  

                    # Подсчет общей калорийности на основе количества
                    ingredient_calories = (quantity * unit_calories).quantize(Decimal('0.01'), rounding=ROUND_UP)
                    total_calories += ingredient_calories
                    ingredient_fats = (quantity * unit_fats)
                    total_fats += ingredient_fats
                    ingredient_carbohydrates = (quantity * unit_carbohydrates)
                    total_carbohydrates += ingredient_carbohydrates
                    ingredient_proteins = (quantity * unit_proteins)
                    total_proteins += ingredient_proteins


            # calories category set

            if total_calories < 200:
                category = Category.objects.get(name='До 200 ккал')
                self.object.categories.add(category)

            elif total_calories < 400:
                category = Category.objects.get(name='200 - 400 ккал')
                self.object.categories.add(category)

            elif total_calories < 400:
                category = Category.objects.get(name='400 - 600 ккал')
                self.object.categories.add(category)

            elif total_calories < 800:
                category = Category.objects.get(name='600 - 800 ккал')
                self.object.categories.add(category)
            
            else:
                category = Category.objects.get(name='Более 800 ккал')
                self.object.categories.add(category)


            # time set
            
            time = form.cleaned_data.get('cooking_time')
            if time > 60:
                hour = time // 60
                minutes = time % 60
                if minutes == 0:
                    self.object.cooking_time_text = f'{hour} час'
                else:
                    self.object.cooking_time_text = f'{hour} час {minutes} мин'
            else:
                self.object.cooking_time_text = f'{time} мин'
            




            self.object.recipe_calories = total_calories
            self.object.recipe_fats = total_fats
            self.object.recipe_carbohydrates = total_carbohydrates
            self.object.recipe_proteins = total_proteins
            self.object.save()

            return redirect(reverse("recipe", kwargs={"pk": self.object.pk}))
        else:
            print("Not valid")
            # Добавляем ошибки, если нет заполненного ингредиента или шага
            if not ingredients_have_data:
                ingredient_formset.non_form_errors().append("Необходимо добавить хотя бы один ингредиент.")
                print("Error added: No ingredients found.")
            if not steps_have_text:
                step_formset.non_form_errors().append("Необходимо добавить хотя бы один шаг рецепта.")
                print("Error added: No steps found.")

            return self.form_invalid(form)
        

    def form_invalid(self, form):
        # Если форма рецепта не валидна, возвращаем ошибочный контекст
        print('Сработала функция инвалид')
        print("POST data:", self.request.POST)

        ingredient_formset = RecipeIngredientFormSet(self.request.POST)
        step_formset = RecipeStepFormSet(self.request.POST)
        selected_categories = self.request.POST.getlist('categories')
        print(selected_categories)


        return self.render_to_response(
            self.get_context_data(form=form, 
                                   ingredient_formset=ingredient_formset, 
                                   step_formset=step_formset,
                                   selected_categories=selected_categories)
        )


class RecipeView(TemplateView):
    template_name = "recipiesapp/recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')  # Получаем pk из URL
        recipe = get_object_or_404(Recipe, pk=pk)  # Получаем рецепт по pk
        context['recipe'] = recipe
        context['ingredients'] = RecipeIngredient.objects.filter(recipe=recipe)
        context['steps'] = RecipeStep.objects.filter(recipe=recipe)
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
    fields = ["name", "short_description", "categories", "image", "cooking_time", "quantity_of_servings"]
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

        # Инициализируем формсет шагов
        step_formset = RecipeStepFormSet(self.request.POST, instance=self.object)

        # Проверка валидности формсета шагов
        if step_formset.is_valid():

            # Проверяем наличие id для существующих объектов
            for step_form in step_formset:
                if not step_form.cleaned_data.get("id") and step_form.instance.pk:
                    step_form.cleaned_data["id"] = step_form.instance.pk

            # Сохранение формсета после валидации и добавления id
            step_formset.save()



            



                       # Подсчет калорий для рецепта
            total_calories = 0
            total_fats = 0
            total_carbohydrates = 0
            total_proteins = 0
            for ingredient_form in ingredient_formset:
                # Проверка, что product и quantity присутствуют в cleaned_data
                if 'product' in ingredient_form.cleaned_data and 'quantity' in ingredient_form.cleaned_data:
                    unit_of_measurement = ingredient_form.cleaned_data['unit_of_measurement']

                    match unit_of_measurement:
                        case 'Ч.л':
                            quantity = Decimal(ingredient_form.cleaned_data['quantity'] * 5)
                        case 'С.л':
                            quantity = Decimal(ingredient_form.cleaned_data['quantity'] * 15)
                        case 'По вкусу':
                            quantity = 0
                        case _:
                            quantity = Decimal(ingredient_form.cleaned_data['quantity'])
                    
                    product = ingredient_form.cleaned_data['product']
                    unit_calories = Decimal(product.calories / 100)  # калорийность продукта на единицу измерения
                    unit_fats = Decimal(product.fats / 100)
                    unit_carbohydrates = Decimal(product.carbohydrates / 100)
                    unit_proteins = Decimal(product.proteins / 100)  

                    # Подсчет общей калорийности на основе количества
                    ingredient_calories = (quantity * unit_calories).quantize(Decimal('0.01'), rounding=ROUND_UP)
                    total_calories += ingredient_calories
                    ingredient_fats = (quantity * unit_fats)
                    total_fats += ingredient_fats
                    ingredient_carbohydrates = (quantity * unit_carbohydrates)
                    total_carbohydrates += ingredient_carbohydrates
                    ingredient_proteins = (quantity * unit_proteins)
                    total_proteins += ingredient_proteins

            # Сохраняем выбранные категории
            form.cleaned_data['categories'] = form.cleaned_data.get('categories')
            self.object.categories.set(form.cleaned_data['categories'])


            if total_calories < 200:
                category = Category.objects.get(name='До 200 ккал')
                self.object.categories.add(category)

            elif total_calories < 400:
                category = Category.objects.get(name='200 - 400 ккал')
                self.object.categories.add(category)

            elif total_calories < 400:
                category = Category.objects.get(name='400 - 600 ккал')
                self.object.categories.add(category)

            elif total_calories < 800:
                category = Category.objects.get(name='600 - 800 ккал')
                self.object.categories.add(category)
            
            else:
                category = Category.objects.get(name='Более 800 ккал')
                self.object.categories.add(category)



            # time set
            
            time = form.cleaned_data.get('cooking_time')
            if time > 60:
                hour = time // 60
                minutes = time % 60
                if minutes == 0:
                    self.object.cooking_time_text = f'{hour} час'
                else:
                    self.object.cooking_time_text = f'{hour} час {minutes} мин'
            else:
                self.object.cooking_time_text = f'{time} мин'


            self.object.recipe_calories = total_calories
            self.object.recipe_fats = total_fats
            self.object.recipe_carbohydrates = total_carbohydrates
            self.object.recipe_proteins = total_proteins
            self.object.save()



            return redirect(reverse("recipe", kwargs={"pk": self.object.pk}))
        else:
            # Логирование ошибок для отладки
            print("Ошибки formset:")
            for i, f in enumerate(ingredient_formset.forms):
                print(f"Форма ингредиента {i}: ошибки: {f.errors}")
                if 'id' in f.errors:
                    print(f"Поле 'id' формы ингредиента {i}: значение = {f['id'].value()}")

            return self.render_to_response(
                self.get_context_data(form=form, ingredient_formset=ingredient_formset, step_formset=step_formset)
            )


    def test_func(self):
        # Ограничение доступа только для автора рецепта
        return self.request.user == self.get_object().author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredient_formset'] = RecipeIngredientFormSet(instance=self.object)  # Подключаем formset ингредиентов
        context['selected_categories'] = self.object.categories.values_list('id', flat=True)
        context['step_formset'] = RecipeStepFormSet(instance=self.object)
        return context

    def form_invalid(self, form):
        # Возвращаем контекст с ошибками, если основная форма рецепта не валидна
        ingredient_formset = RecipeIngredientFormSet(self.request.POST)
        return self.render_to_response(
            self.get_context_data(form=form, ingredient_formset=ingredient_formset)
        )
    

class AddProductView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = "recipiesapp/add_product.html"
    success_url = reverse_lazy("add_recipe")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return redirect(reverse_lazy("add_recipe"))
        
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
        