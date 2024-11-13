# Generated by Django 5.1.2 on 2024-11-08 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipiesapp', '0017_recipe_cooking_time_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit_of_measurement',
            field=models.CharField(choices=[('Гр', 'Гр'), ('Мл', 'Мл'), ('Ч.л', 'Ч.л'), ('С.л', 'С.л'), ('По вкусу', 'По вкусу')], max_length=8),
        ),
    ]