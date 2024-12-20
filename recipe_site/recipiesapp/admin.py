from django.contrib import admin
from .models import Recipe, Category, Product, RecipeIngredient, RecipeStep# устанавливаем связь с моделями, которые мы хотим отобразить
from mptt.admin import MPTTModelAdmin

# Register your models here.


class CategoryInline(admin.TabularInline):
    model = Recipe.categories.through


class RecipeIngridientsline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


class RecipeStepsline(admin.TabularInline):
    model = RecipeStep
    extra = 0


@admin.register(Recipe) # Этим декаратором мы регистрируем модель
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
        RecipeIngridientsline,
        RecipeStepsline,
    ]

    list_display = [
        'name', 
        'short_description', 
        'author', 
        'image', 
        'cooking_time', 
        'cooking_time_text',
        'quantity_of_servings',
        'recipe_calories',
        'recipe_fats',
        'recipe_carbohydrates',
        'recipe_proteins',
        'creation_time',
        'update_time',
        ] # тут мы добавляем колонки, которые хотим отоборазить
    
    search_fields = ['name'] # это для добавления поиска
    search_help_text = 'Поиск по имени или цене продукта' # это описание поиска
    readonly_fields = ['creation_time', 'update_time']

    fieldsets = [
        (
            'Recipe info', 
            {
                'classes': ['wide'],
                'description': 'Main info',
                'fields': ['name', 'author', 'short_description', 'image'],
            },
        ),
        (
            'Recipe body', 
            {
                'classes': ['wide'],
                'description': 'Main info',
                'fields': ['cooking_time', 'cooking_time_text',  'quantity_of_servings'],
            },
        ),
        (
            'Recipe КБЖУ', 
            {
                'classes': ['wide'],
                'description': 'Main info',
                'fields': ['recipe_calories', 'recipe_fats', 'recipe_carbohydrates', 'recipe_proteins'],
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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'name', 
        'author', 
        'calories', 
        'fats',
        'carbohydrates', 
        'proteins', 
        ] 
    search_fields = ['name'] # это для добавления поиска
    search_help_text = 'Поиск по имени или цене продукта' # это описание поиска
    readonly_fields = ['creation_time', 'update_time']

    fieldsets = [
        (
            'Recipe info', 
            {
                'classes': ['wide'],
                'description': 'Main info',
                'fields': ['name', 'author'],
            },
        ),
                (
            'Recipe body', 
            {
                'classes': ['wide'],
                'description': 'Main info',
                'fields': ['calories', 'fats', 'carbohydrates', 'proteins'],
            },
        ),

    ]


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'recipe', 
        'product', 
        'quantity', 
        'unit_of_measurement',
        ] 
    search_fields = ['recipe'] # это для добавления поиска
    search_help_text = 'Поиск по имени или цене продукта' # это описание поиска
    readonly_fields = ['creation_time', 'update_time']

    fieldsets = [
        (
            'Recipe info', 
            {
                'classes': ['wide'],
                'description': 'Main info',
                'fields': ['recipe', 'product', 'quantity', 'unit_of_measurement'],
            },
        ),
    ]


@admin.register(RecipeStep)
class RecipeStepientAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'recipe', 
        'text', 
        ] 
    search_fields = ['recipe'] # это для добавления поиска
    search_help_text = 'Поиск по имени или цене продукта' # это описание поиска
    readonly_fields = ['creation_time', 'update_time']

    fieldsets = [
        (
            'Recipe info', 
            {
                'classes': ['wide'],
                'description': 'Main info',
                'fields': ['recipe', 'text'],
            },
        ),
    ]
