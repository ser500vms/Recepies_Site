# Generated by Django 5.1.2 on 2024-11-08 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipiesapp', '0019_alter_recipeingredient_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
