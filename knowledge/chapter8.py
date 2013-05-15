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



