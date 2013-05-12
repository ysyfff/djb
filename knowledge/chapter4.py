'''The template system is just a Python library that you can use anywhere,
not just in Django views.'''

#example#

from django import template
t = template.Template('My name is {{ name }}.')
# c = template.Context({'name': 'Adrian'})
print t.render(c)
My name is Adrian.
c = template.Context({'name': 'Fred'})
print t.render(c)
# My name is Fred.