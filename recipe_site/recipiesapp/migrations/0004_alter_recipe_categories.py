# Generated by Django 5.1.2 on 2024-10-31 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipiesapp', '0003_alter_recipe_options_recipe_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='recipe', to='recipiesapp.category'),
        ),
    ]
