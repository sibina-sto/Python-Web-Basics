from django.shortcuts import render, redirect

from Recipes.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from Recipes.web.models import Recipe


def show_index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }
    return render(request, 'delete.html', context)


def show_recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(',')
    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'details.html', context)
