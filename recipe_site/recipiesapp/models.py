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
    ingridients = models.TextField(blank=False)
    cooking_steps = models.TextField(blank=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        # Сначала выполняется сортировка по имени, затем — по возрасту
        ordering = ('-creation_time',)

    def __str__(self):
        return f'Рецепт: {self.name}'




