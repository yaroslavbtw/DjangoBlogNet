from django import template
from django.shortcuts import get_object_or_404
from women.models import *
from women.views import menu

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def find_categories_slug(cat_id=None):
    category = get_object_or_404(Category, pk=cat_id)
    return category.slug


@register.simple_tag()
def get_menu():
    return menu