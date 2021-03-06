from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from apps.home.api import *
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(StudentResource())

urlpatterns = patterns('',

	(r'^api/', include(v1_api.urls)),
    # Examples:
    # url(r'^$', 'students.views.home', name='home'),
    # url(r'^students/', include('students.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
