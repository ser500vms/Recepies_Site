from django.urls import path
from .views import RecipeView, AddRecipeView

urlpatterns = [
    path('add-recipe/', AddRecipeView.as_view(), name='add_recipe'),
    path('recipe/', RecipeView.as_view(), name='recipe'),
]
