from django.conf.urls import patterns, include, url
from txrd.views import portal, login_member, logout_member, portal_points

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'txrdHRApp.views.home', name='home'),
    # url(r'^txrdHRApp/', include('txrdHRApp.foo.urls')),
    url(r'^$', portal),
    url(r'^portal/$', portal),
    url(r'^portal/points/$', portal_points),
    url(r'^login/$', login_member),
    url(r'^logout/$', logout_member),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)
