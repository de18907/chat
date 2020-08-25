from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo(value):
    if len(value) >= 8:
        largo = '<p>tu nombre es muy largo</p>'
    else:
        largo = ''
    return f"<h1>Bienvenido, {value}</h1>"+largo
