from django import template

register = template.Library()

@register.filter
def reverse_string(value):
    return value[::-1]

@register.filter
def multiply(value, arg):
    try:
        return value * int(arg)
    except (ValueError, TypeError):
        return value

@register.simple_tag
def greeting(name="Гость"):
    return f"Привет, {name}!"

@register.simple_tag
def percentage(part, total):
    try:
        return round((int(part) / int(total)) * 100, 2)
    except (ZeroDivisionError, ValueError):
        return 0
