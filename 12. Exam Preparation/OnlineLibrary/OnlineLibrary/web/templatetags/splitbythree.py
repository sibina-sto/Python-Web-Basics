from django import template

register = template.Library()


@register.filter
def splitbythree(given_list):
    return [given_list[i:i+3] for i in range(0, len(given_list), 3)]
