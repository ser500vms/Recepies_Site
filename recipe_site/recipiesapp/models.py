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
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, related_name='recipe', null=True)

    # class Meta:
    #     # Сначала выполняется сортировка по имени, затем — по возрасту
    #     ordering = ('-creation_time',)

    def __str__(self):
        return f'Рецепт: {self.name}'




