from django import template
from myplantapp.models import PlantModel

register = template.Library()


@register.filter(name="price_filter")
def price_filter(price):
    return "%.2f" %price