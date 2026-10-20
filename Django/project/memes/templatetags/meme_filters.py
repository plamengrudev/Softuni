from django import template
from django.template.defaultfilters import stringfilter
from django.utils.text import slugify

register = template.Library()

@register.filter
@stringfilter
def hashtag(value):
    tag=slugify(value).replace("-","_")
    return f"#{tag}" if tag else ""