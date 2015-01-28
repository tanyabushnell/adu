from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'guest_house.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ajax', 'guest_house.views.ajax', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dom?$', 'guest_house.views.dom', name='dom')
)
