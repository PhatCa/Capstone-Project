from django import forms
from . import models

class CreateRecipe(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['name','ingredient','instructions','picture']
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'ingredient' : forms.TextInput(attrs={'class':'form-control'}),
            'instructions' : forms.TextInput(attrs={'class':'form-control'}),
            'picture' : forms.TextInput(attrs={'class':'form-control'}),

        }