from django.shortcuts import render
from django.views import generic as views

from fruitipedia.fruit.models import Fruit


class Index(views.TemplateView):
    template_name = 'common/index.html'


class Dashboard(views.ListView):
    model = Fruit
    template_name = 'common/dashboard.html'
