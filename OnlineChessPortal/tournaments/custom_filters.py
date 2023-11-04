from django import template

register = template.Library()

@register.filter
def count_elements(value, delimiter=','):
    if value:
        return len(value.split(delimiter))
    return 0
