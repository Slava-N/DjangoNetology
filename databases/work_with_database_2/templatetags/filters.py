from django import template
import math

register = template.Library()

@register.filter
def translateLte(value):
    translate = {'True':"Да", "False":"Нет"}


    return translate[value]
