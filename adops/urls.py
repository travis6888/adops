from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adops.views.home', name='home'),
    url(r'^$', 'optimize.views.home', name='home'),
    url(r'^home/$', 'optimize.views.home', name='home'),
    url(r'^download/$', 'optimize.views.download', name='download'),

    url(r'upload/$', 'optimize.views.file_upload', name='file_upload'),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)