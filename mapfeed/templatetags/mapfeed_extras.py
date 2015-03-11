from django import template
register = template.Library()

#Returns the next station's x coordinate in the path
#@register.filter(name='nextstationx')
@register.simple_tag
def nextstationx(*args, **kwargs):
    next = i + 1
    return paths[next].station.x_coord

@register.filter(name='nextstationy')
def nextstationy(value, arg):
    next = arg + 1
    return value[next].station.y_coord
