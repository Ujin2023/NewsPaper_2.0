from django import template

register = template.Library()

censor = ['редиска', ]

@register.filter()
def censor_filter(value):
    if isinstance(value, str):
        for i in value.split():
            if i.lower() in censor:
                value =  value.replace(i, ''.join(f"{i[0]}***"))
    return value