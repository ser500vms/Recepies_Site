# Generated by Django 5.1.2 on 2024-11-05 14:21

import recipiesapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipiesapp', '0014_remove_recipe_cooking_steps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to=recipiesapp.models.recipe_image_upload_path),
        ),
    ]