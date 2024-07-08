from django import template

register = template.Library()

@register.filter
def filter(clases, profesor_id):
    return [clase for clase in clases if clase.profesor_id == profesor_id]
