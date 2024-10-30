from django.contrib import admin
from .models import Recipe, Category# устанавливаем связь с моделями, которые мы хотим отобразить
from mptt.admin import MPTTModelAdmin

# Register your models here.


class CategoryInline(admin.TabularInline):
    model = Recipe.categories.through



@admin.register(Recipe) # Этим декаратором мы регистрируем модель
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

    list_display = [
        'name', 
        'short_description', 
        # 'ingridients', 
        # 'cooking_steps', 
        # 'cooking_time', 
        # 'creation_time',
        # 'updated_at', 
        # 'author',
        # 'recipe_img',
        ] # тут мы добавляем колонки, которые хотим отоборазить
    
    search_fields = ['name'] # это для добавления поиска
    search_help_text = 'Поиск по имени или цене продукта' # это описание поиска
    # readonly_fields = ['creation_time', 'updated_at']

    fieldsets = [
        (
            'Recipe info', 
            {
                'classes': ['wide'],
                'description': 'Main info',
                'fields': ['name', 'short_description'],
            },
        ),

    ]

    # actions = [
    #     reset_discount, 
    #     give_discount,
    # ]
    

    def short_description(self, obj: Recipe): # функция для сокращения отображения поля с описанием
        if len(obj.short_description) < 48:
            return obj.short_description
        return f'{obj.short_description[:48]} ...'
    

@admin.register(Category)
class SubCategoryAdmin(MPTTModelAdmin):
    list_display = ['id', 'name', 'parent'] 


