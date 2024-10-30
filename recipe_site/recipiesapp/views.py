from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RecipeForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from django.views.generic import (
    TemplateView, 
    CreateView,
    DeleteView,
    UpdateView,
    ListView
)
from .forms import RecipeForm


class AddRecipeView(CreateView):
    form_class = RecipeForm
    template_name = "recipiesapp/add-recipe.html"
    success_url = reverse_lazy("recipe")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Убираем предзаполнение данных при GET-запросе
        if self.request.method == 'GET':
            kwargs.update({'instance': None})
        return kwargs


class RecipeView(TemplateView):
    template_name = "recipiesapp/recipe.html"