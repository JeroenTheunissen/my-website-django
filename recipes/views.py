from django.shortcuts import render
from .models import Recipe

def home(request):
    return render(request, "recipes/home.html")

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})

