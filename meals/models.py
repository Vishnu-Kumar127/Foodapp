from django.db import models
from django.utils.text import slugify

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    description = models.TextField(blank=True)  # Add the description column
    ingredients = models.TextField()  # Comma-separated ingredients
    dietary_preferences = models.CharField(max_length=200)  # E.g., "vegan, keto"
    preparation_time = models.IntegerField()  # In minutes
    difficulty = models.CharField(max_length=50)  # E.g., "Easy", "Medium", "Hard"
    nutrition = models.JSONField(null=True, blank=True)  # Nutritional info in JSON format
    instructions = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Auto-generate slug based on recipe name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
