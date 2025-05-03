from django import template
import random

register = template.Library()

@register.filter(name='shout')
def shout(value):
    if isinstance(value, str):
        return value.upper() + "!"
    return value

@register.filter(name='remove_spaces')
def remove_spaces(value):
    if isinstance(value, str):
        return value.replace(" ", "")
    return value

@register.simple_tag(name='multiply')
def multiply(a, b):
    try:
        return float(a) * float(b)
    except:
        return ''

@register.simple_tag(name='random_choice')
def random_choice(*args):
    return random.choice(args) if args else ''