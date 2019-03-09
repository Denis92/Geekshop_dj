from django import template
# from django.conf import settings

register = template.Library()


@register.filter(name='mull_tag')
def mull_tag(val_1, val_2):
    return val_1 * val_2
