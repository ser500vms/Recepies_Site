from django import forms
from .models import Recipe, Category
from mptt.forms import TreeNodeMultipleChoiceField



class RecipeForm(forms.ModelForm):
    categories = TreeNodeMultipleChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Recipe
        fields = [
            'name', 
            'image', 
            'short_description',
            'categories', 
            'cooking_time', 
            'quantity_of_servings',
            'ingridients', 
            'cooking_steps',
            ]

