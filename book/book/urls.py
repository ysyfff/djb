from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from books import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'book.views.home', name='home'),
    # url(r'^book/', include('book.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'books.views.search'),
    url(r'^contact/$', 'contact.views.contact'),
    url(r'^html_send/$', 'contact.views.html_send'),
)
