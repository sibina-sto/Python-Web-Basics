from django import forms
from django.core.exceptions import ValidationError

from Recipes.web.models import Recipe
from Recipes.web.validators import regex_validator


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def clean_ingredients(self):
        ingredients = self.cleaned_data['ingredients']
        regex_validator(ingredients)

        return ingredients


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def clean_ingredients(self):
        ingredients = self.cleaned_data['ingredients']
        regex_validator(ingredients)

        return ingredients


class DeleteRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        fields = '__all__'
