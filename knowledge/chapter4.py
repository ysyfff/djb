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


'''The manage.py shell command has one key difference:
before starting the interpreter, it tells Django which settings file to use.
Many parts of Django, including the template system, rely on your settings,
and you won’t be able to use them unless the framework knows which settings to use.
'''
