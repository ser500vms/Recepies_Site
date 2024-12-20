from django.urls import path
from .views import RecipeView, AddRecipeView, RecipeDeleteView, RecipeUpdateView, product_autocomplete, AddProductView

urlpatterns = [
    path('add-recipe/', AddRecipeView.as_view(), name='add_recipe'),
    path('add-product/', AddProductView.as_view(), name='add_product'),
    path('product-autocomplete/', product_autocomplete, name='product_autocomplete'),
    path('recipe/<int:pk>', RecipeView.as_view(), name='recipe'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='delete_recipe'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='update_recipe'),
]
