from django import forms
from .models import Product, Recipe, Category, RecipeIngredient, RecipeStep
from mptt.forms import TreeNodeMultipleChoiceField
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.exceptions import ValidationError


def validate_file(file: InMemoryUploadedFile) -> None:
    allowed_size = 1 * 1024 * 1024  # 1 Mb
    if file.name and "virus" in file.name:
        raise ValidationError("file name shod not consist 'virus'")
    if file.size > allowed_size:
        raise ValidationError("file size is too big. 1Mb limit'")


class RecipeForm(forms.ModelForm):
    categories = TreeNodeMultipleChoiceField(queryset=Category.objects.all(), required=False)     
    image = forms.ImageField(validators=[validate_file])

    class Meta:
        model = Recipe
        fields = [
            'name', 
            'image', 
            'short_description',
            'categories', 
            'cooking_time', 
            'quantity_of_servings',
            ]
        labels = {
            'name': 'Название рецепта',
            'image': 'Изображение',
            'short_description': 'Краткое описание рецепта',
            'categories': 'Выбирете категории',
            'cooking_time': 'Время приготовления',
            'quantity_of_servings': 'Количество порций',
        }


class RecipeIngredientForm(forms.ModelForm):

    class Meta:
        model = RecipeIngredient
        fields = ['product', 'quantity', 'unit_of_measurement']

        labels = {
            'product': 'Выберите продукт',
            'quantity': 'Количество',
            'unit_of_measurement': 'Еденица измерения',
        }




class RecipeStepForm(forms.ModelForm):
    class Meta:
        model = RecipeStep
        fields = ['text']

        labels = {
            'text': 'Шаг',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].required = True


class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = ['name', 'calories', 'fats', 'carbohydrates', 'proteins']

