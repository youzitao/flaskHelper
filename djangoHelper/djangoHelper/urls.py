from django.conf.urls import patterns, include, url
from django.contrib import admin

import rest_api

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoHelper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   url('api/', include('rest_api.urls')),
)
