from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'railtracker.views.home', name='home'),
    # url(r'^railtracker/', include('railtracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mapfeed/$', 'mapfeed.views.index'),
    url(r'^mapfeed/(?P<city_id>\d+)/$', 'mapfeed.views.details'),
    url(r'^mapfeed/(?P<city_id>\d+)/(?P<line_id>\d)$', 'mapfeed.views.line'),
)
