from django import template
from babel.numbers import format_currency
register = template.Library()

@register.filter
def get(row, key):
	return row[key]

@register.filter
def as_currency_plain(value):
	# print('trying to format '+str(value)+' of type '+str(type(value)))
	try:
		return format_currency(int(value), 'TRY', u'#,##0.00 ¤', locale='tr_TR')
	except:
		return "wtf"

@register.filter
def as_currency_plain_short(value):
	# print('trying to format '+str(value)+' of type '+str(type(value)))
	try:
		return format_currency(int(value), 'TRY', u'#,##0', locale='tr_TR').split(',')[0]
	except:
		return "wtf"

@register.simple_tag
def as_currency(value, left_right = None):
	_res = format_currency(value, 'TRY', u'#,##0.00 ¤', locale='tr_TR')
	if left_right == 'left':
		return _res.split(',')[0]
	elif left_right == 'right':
		return ','+_res.split(',')[1]
	else:
		return _res

@register.filter
def as_percentage(value):
	return "%{:.2f}".format(value).replace('.',',')

@register.filter
def as_int(value):
	return int(value)

@register.filter
def add_tenure_suffix(value):
	if int(value) % 12 == 0:
		return str(int(value)) + " ay (" + str(int(int(value)/12)) +" yıl)"
	else:
		return str(int(value)) + " ay"

@register.filter
def add_tenure_suffix_plain(value):
	return str(int(value)) + " ay"

@register.filter
def replace_blanks(value):
	return value.replace(' ','@')

@register.simple_tag
def weight(value, nrows):
	return str(int(round(1-(value/nrows/3),2)*100))+"%"

@register.simple_tag
def concat(c1, c2, c3=None):
	return str(c1)+str(c2)+str(c3)

@register.simple_tag
def concat_interests(i1,i2):
	if i1==i2:
		return "%{:.2f}".format(i1).replace('.',',')
	else:
		return "%{:.2f}".format(i1).replace('.',',') + " - " + "%{:.2f}".format(i2).replace('.',',')