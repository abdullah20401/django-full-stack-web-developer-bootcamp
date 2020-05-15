from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

@register.filter(name='underscore')
def underscore(value):
    """
    This removes all the underscores out from the string!
    """
    return value.replace('_', ' ')

# register.filter('cut', cut)