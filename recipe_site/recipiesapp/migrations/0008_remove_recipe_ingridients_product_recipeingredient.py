# Generated by Django 5.1.2 on 2024-10-31 15:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipiesapp', '0007_alter_recipe_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingridients',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calories', models.PositiveIntegerField()),
                ('fats', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=6)),
                ('proteins', models.DecimalField(decimal_places=2, max_digits=6)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unit_of_measurement', models.CharField(choices=[('GR', 'Гр'), ('ML', 'Мл'), ('TIS', 'ч.л'), ('TS', 'с.л'), ('T', 'Шт'), ('OT', 'По вкусу')], max_length=3)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipiesapp.product')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredients', to='recipiesapp.recipe')),
            ],
            options={
                'unique_together': {('recipe', 'product')},
            },
        ),
    ]
