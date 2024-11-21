from django.utils import timezone
import os
from uuid import uuid4
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.


def recipe_image_upload_path(instance, filename):
    # Получаем текущий год
    timestamp = timezone.now().strftime('%Y_%m_%d_%H_%M_%S')
    # Получаем расширение оригинального файла
    extension = os.path.splitext(filename)[1]
    # Генерируем уникальное имя файла с годом и уникальным идентификатором
    new_filename = f"{instance.author.username}_{timestamp}_{uuid4().hex}{extension}"
    # Возвращаем путь сохранения
    return os.path.join('users_recipes_img', new_filename)


class Category(MPTTModel):
    name = models.CharField(max_length=50, blank=False)
    parent = TreeForeignKey(
        'self', 
        related_name='children',
        on_delete=models.SET_NULL, 
        null=True,
        blank=True
        )
    
    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return f'Категория: {self.name}'


class Recipe(models.Model):
    name = models.CharField(max_length=50, blank=False)
    short_description = models.CharField(max_length=200, blank=False)
    categories = models.ManyToManyField(Category, related_name='recipe', blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=recipe_image_upload_path, blank=False)
    cooking_time = models.PositiveIntegerField(blank=False)
    cooking_time_text = models.CharField(max_length=20, blank=False)
    quantity_of_servings = models.PositiveIntegerField(default=1, blank=False)
    recipe_calories = models.PositiveIntegerField(blank=True, null=True)
    recipe_fats = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    recipe_carbohydrates = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    recipe_proteins = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        # Сначала выполняется сортировка по имени, затем — по возрасту
        ordering = ('-creation_time',)

    def __str__(self):
        return f'Рецепт: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    calories = models.PositiveIntegerField(blank=False, default=0)
    fats = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    proteins = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):

    MEASUREMENT_CHOICES = {
    "Гр": "Гр",
    "Мл": "Мл",
    "Ч.л": "Ч.л",
    "С.л": "С.л",
    "По вкусу": "По вкусу",
}
    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False) # подумать каскад или сет нал
    quantity =  models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0)
    unit_of_measurement = models.CharField(max_length=8, choices=MEASUREMENT_CHOICES, blank=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        product_name = self.product.name if self.product else "Unknown Product"
        recipe_name = self.recipe.name if self.recipe else "Unknown Recipe"
        return f"{self.quantity} {self.get_unit_of_measurement_display()} {product_name} для {recipe_name}"
    

class RecipeStep(models.Model):
    text = models.TextField(blank=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_steps')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)