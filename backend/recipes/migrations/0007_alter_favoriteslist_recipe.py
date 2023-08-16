# Generated by Django 3.2.13 on 2023-08-15 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_alter_shoppinglist_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteslist',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='recipes.recipe', verbose_name='рецепт'),
        ),
    ]
