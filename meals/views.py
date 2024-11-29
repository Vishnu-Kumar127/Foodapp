from django.http import JsonResponse
from .models import Recipe
from django.shortcuts import render,get_object_or_404

def find_recipe(request):
    user_ingredients = request.GET.get('ingredients', '').split(',')
    user_ingredients = {ingredient.strip().lower() for ingredient in user_ingredients}  # Convert to a set for faster lookup

    recipes = Recipe.objects.all()

    matched_recipes = []

    for recipe in recipes:
        recipe_ingredients = {ingredient.strip().lower() for ingredient in recipe.ingredients.split(',')}

        if recipe_ingredients.issubset(user_ingredients):
            recipe_url = f"/recipe/{recipe.slug}/"
            matched_recipes.append(
                {
                    "name": recipe.name,
                    "description": recipe.description,
                    "link": recipe_url
                }
            )

    if matched_recipes:
        return JsonResponse({
            "recipes": matched_recipes
        })
    else:
        return JsonResponse({
            "message": "No recipes found with these ingredients"
        })

def recipe_list(request):
    search_query = request.GET.get('search', '').strip()
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
    recipe = get_object_or_404(Recipe, slug=slug)

    # Split ingredients and instructions
    ingredients_list = [ingredient.strip() for ingredient in recipe.ingredients.split(',') if ingredient.strip()]
    instructions_list = [instruction.strip() for instruction in recipe.instructions.split(',') if instruction.strip()]

    # Nutrition data, fallback to empty dictionary if None
    nutrition_dict = recipe.nutrition or {}

    return render(request, 'meals/recipe_detail.html', {
        'recipe': recipe,
        'ingredients_list': ingredients_list,
        'instructions_list': instructions_list,
        'nutrition_dict': nutrition_dict,
    })