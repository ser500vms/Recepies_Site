from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.


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
    image = models.ImageField(upload_to='users_recipes_img', blank=False)
    cooking_time = models.PositiveIntegerField(blank=False)
    quantity_of_servings = models.PositiveIntegerField(default=1, blank=False)
    recipe_calories = models.PositiveIntegerField(blank=True, null=True)
    cooking_steps = models.TextField(blank=False)
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
    calories = models.PositiveIntegerField(blank=False)
    fats = models.DecimalField(max_digits=6, decimal_places=2)
    carbohydrates = models.DecimalField(max_digits=6, decimal_places=2)
    proteins = models.DecimalField(max_digits=6, decimal_places=2)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):

    MEASUREMENT_CHOICES = {
    "GR": "Гр",
    "ML": "Мл",
    "TIS": "ч.л",
    "TS": "с.л",
    "T": "Шт",
    "OT": "По вкусу",
}
    
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =  models.DecimalField(max_digits=6, decimal_places=2)
    unit_of_measurement = models.CharField(max_length=3, choices=MEASUREMENT_CHOICES)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} {self.get_unit_of_measurement_display()} {self.product.name} для {self.recipe.name}"