from django import forms
from .models import Recipe, Category
from mptt.forms import TreeNodeMultipleChoiceField



class RecipeForm(forms.ModelForm):
    categories = TreeNodeMultipleChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Recipe
        fields = ['name', 'short_description', 'categories']

