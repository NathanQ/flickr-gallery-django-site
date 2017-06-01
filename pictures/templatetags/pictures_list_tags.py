from django import template
from pictures.models import Set

register = template.Library()


@register.inclusion_tag('list.html')
def set_list():
    sets = Set.objects.all()
    return {'sets': sets}
