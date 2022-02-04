from django import template
from service.models import Service




register = template.Library()


@register.simple_tag(name='get_services')
def get_services():
    return Service.objects.all()



