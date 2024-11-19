from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        recipes = Recipe.objects.filter(name__icontains=search_query)
        heading = "Searched Recipes"
    else:
        recipes = Recipe.objects.all()
        heading = "All Recipes"

    return render(request, 'meals/recipe_list.html', {
        'recipes': recipes,
        'heading': heading
    })


def recipe_detail(request, slug):
    # Retrieve the recipe object using the slug
    recipe = Recipe.objects.get(slug=slug)
    
    # Split ingredients from a comma-separated string
    ingredients_list = recipe.ingredients.split(',')
    
    # Split instructions by comma into individual steps
    instructions_list = recipe.instructions.split(',')  # Split the comma-separated string into a list
    
    # If nutrition is already stored as a dictionary, use it directly
    nutrition_dict = recipe.nutrition  # Assuming `nutrition` is a dictionary in the model
    
    return render(request, 'meals/recipe_detail.html', {
        'recipe': recipe,
        'ingredients_list': ingredients_list,
        'instructions_list': instructions_list,  # Pass the instructions list
        'nutrition_dict': nutrition_dict,  # Pass the nutrition dictionary
    })
