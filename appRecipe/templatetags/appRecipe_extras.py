from django import template
register = template.Library()

indexTemp = 0;

@register.filter
def init(obj):
	global indexTemp
	indexTemp = 1
	return ''

@register.filter
def next(obj):
	global indexTemp
	indexTemp = indexTemp+1
	return indexTemp

@register.filter
def classname(obj):
  classname = obj.__class__.__name__
  return classname

@register.filter    
def subtract(value, arg):
    return int(value) - int(arg)
