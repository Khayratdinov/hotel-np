from django import template
from blog.models import Category_Blog, Tag_Blog, Blog



register = template.Library()


@register.simple_tag(name='get_categories')
def get_categories():
    return Category_Blog.objects.all()

@register.simple_tag(name='get_tags')
def get_tags():
    return Tag_Blog.objects.all()


@register.simple_tag(name='get_blog')
def get_blog():
    return Blog.objects.all().order_by('?')[:3]