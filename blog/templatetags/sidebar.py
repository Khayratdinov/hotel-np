from django import template
from blog.models import Category, Tag, Blog



register = template.Library()


@register.simple_tag(name='get_categories')
def get_categories():
    return Category.objects.all()

@register.simple_tag(name='get_tags')
def get_tags():
    return Tag.objects.all()


@register.simple_tag(name='get_blog')
def get_blog():
    return Blog.objects.all().order_by('?')[:3]