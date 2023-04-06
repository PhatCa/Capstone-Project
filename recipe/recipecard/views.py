from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.decorators import login_required
from . import forms
import json
import requests
# Create your views here.

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
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('recipes:list')

    else:    
        form = forms.CreateRecipe
    return render(request,'recipecard/recipe_create.html',{'form':form})
