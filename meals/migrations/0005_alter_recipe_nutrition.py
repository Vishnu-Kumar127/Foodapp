# Generated by Django 5.0.4 on 2024-11-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0004_alter_recipe_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='nutrition',
            field=models.JSONField(blank=True, default=dict, help_text="JSON format for nutrition info (e.g., {'Calories': 200, 'Protein': '10g'}).", null=True),
        ),
    ]