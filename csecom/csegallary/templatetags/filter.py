import markdown
from django import template
from django.utils.safestring import mark_safe
from PIL import Image
from django.urls import reverse
import datetime

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))


@register.filter()
def img(value):
    res = Image.open(value)
    if res.width >= 900 or res.height >= 550:
        return res