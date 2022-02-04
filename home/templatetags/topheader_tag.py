from django import template
from home.models import Informations



register = template.Library()


@register.simple_tag(name='get_informations')
def get_informations():
    return Informations.objects.all().order_by('?')[:1]

