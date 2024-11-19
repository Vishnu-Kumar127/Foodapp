from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Recipe

@receiver(post_save, sender=Recipe)
def recipe_saved(sender, instance, created, **kwargs):
    if created:
        print(f"Recipe '{instance.name}' was created!")
    else:
        print(f"Recipe '{instance.name}' was updated!")
