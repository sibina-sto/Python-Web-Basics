from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from .models import Fruit


class FruitCreate(views.CreateView):
    form_class = FruitCreateForm
    template_name = 'fruit/create-fruit.html'
    success_url = reverse_lazy('dashboard')


class FruitDetails(views.DetailView):
    model = Fruit
    template_name = 'fruit/details-fruit.html'


class FruitEdit(views.UpdateView):
    model = Fruit
    form_class = FruitEditForm
    template_name = 'fruit/edit-fruit.html'
    success_url = reverse_lazy('dashboard')


class FruitDelete(views.DeleteView, FruitEdit):
    model = Fruit
    form_class = FruitDeleteForm
    template_name = 'fruit/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super(FruitEdit, self).get_context_data(**kwargs)
        return context
