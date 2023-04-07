from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from . import forms
import json
import requests
# Create your views here.

#iJlhrcEhWmmtl93uiqrUYcLQYoMLIPiesxI3mepv (api key)


def recipe_list(request):
    recipe = Recipe.objects.all().order_by('id')
    return render(request,'recipecard/recipe_list.html',{'recipes':recipe})

def recipe_detail(request,id):
    recipe = Recipe.objects.get(id=id)
    return render(request,'recipecard/recipe_detail.html', {'recipe':recipe})


@login_required(login_url='/accounts/login/')
def recipe_create(request):
    if request.method == 'POST':
        form = forms.CreateRecipe(request.POST)
        if form.is_valid():
            # Convert ingredient string to array
            ingredient_array = form.cleaned_data['ingredient'].split(", ")

            nutrient_info = {}
            for ingredient in ingredient_array:
                response = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key=iJlhrcEhWmmtl93uiqrUYcLQYoMLIPiesxI3mepv&query={ingredient}")
                newData = response.json()
                nutrients = newData['foods'][1]['foodNutrients']
                for nutrient in nutrients:
                    nutrient_name = nutrient['nutrientName']
                    nutrient_value = nutrient['value']
                    nutrient_unit = nutrient['unitName']
                    if nutrient_name in nutrient_info:
                        nutrient_info[nutrient_name]['value'] += nutrient_value
                    else:
                        nutrient_info[nutrient_name] = {'value': nutrient_value, 'unit': nutrient_unit}


            instance = form.save(commit=False)
            instance.author = request.user
            instance.nutrient_info = nutrient_info  
            instance.save()
            return render(request, 'recipecard/success.html', {'nutrient_info': nutrient_info})



    else:
        form = forms.CreateRecipe()
    return render(request, 'recipecard/recipe_create.html', {'form': form})
