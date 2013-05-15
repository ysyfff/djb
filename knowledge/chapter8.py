# # urls.py
# from django.conf.urls.defaults import *
# from mysite import views

# urlpatterns = patterns('',
#     (r'^(foo)/$', views.foobar_view),
#     (r'^(bar)/$', views.foobar_view),
# )

# # views.py
# from django.shortcuts import render
# from mysite.models import MyModel

# def foobar_view(request, url):
#     m_list = MyModel.objects.filter(is_new=True)
#     if url == 'foo':
#         template_name = 'template1.html'
#     elif url == 'bar':
#         template_name = 'template2.html'
#     return render(request, template_name, {'m_list': m_list})

# urls.py
from django.conf.urls.defaults import *
from mysite import views

urlpatterns = patterns('',
    (r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
    (r'^bar/$', views.foobar_view, {'template_name': 'template2.html'}),
)

# views.py
from django.shortcuts import render
from mysite.models import MyModel

def foobar_view(request, template_name):
    m_list = MyModel.objects.filter(is_new=True)
    return render(request, template_name, {'m_list': m_list})

#-----------------The use of extra keyword in urlconf--------------------------#


# urls.py

from django.conf.urls.defaults import *
from mysite import views

urlpatterns = patterns('',
    (r'^blog/$', views.page),
    (r'^blog/page(?P<num>\d+)/$', views.page),
)

# views.py

def page(request, num='1'):
    # Output the appropriate page of blog entries, according to num.
    # ...

'''
Here, both URL patterns point to the same view – views.
page – but the first pattern doesn’t capture anything from the URL. 
If the first pattern matches, 
the page() function will use its default argument for num, '1'. 
If the second pattern matches, 
page() will use whatever num value was captured by the regular expression.
'''
#-----------------The use of default views arguments------------------------#




