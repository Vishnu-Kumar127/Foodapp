from django.utils.text import slugify
from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(help_text="Comma-separated list of ingredients")
    instructions = models.TextField(help_text="Comma-separated list of instructions")
    nutrition = models.JSONField(help_text="Dictionary of nutrition facts", blank=True, null=True)
    preparation_time = models.PositiveIntegerField(help_text="Time in minutes", blank=True, null=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  
        super().save(*args, **kwargs)

    def _str_(self):
        return self.name

    def get_ingredients_list(self):
        return self.ingredients.split(',')