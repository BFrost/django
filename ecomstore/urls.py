from django.conf.urls import patterns, include, url, handler404
#from django.conf import settings
import settings
import os
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'preview.views.home', name='home'),
    # url(r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('catalog.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^checkout/', include('checkout.urls')),
    (r'^accounts/', include('accounts.urls')),
    (r'^accounts/', include('django.contrib.auth.urls')),
    (r'^search/', include('search.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_ROOT,'static')}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_ROOT,'media')}),
    )
    #urlpatterns += staticfiles_urlpatterns()

handler404 = 'ecomstore.views.file_not_found_404'