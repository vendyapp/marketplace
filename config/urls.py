from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',

    # Admin Url
    # (r'^$', RedirectView.as_view(url='/admin/')),

    # Admin Url
    url(r'^admin/', include(admin.site.urls)),

    # Auth API
    url(r'^api/1/', include('administration.urls')),

    # Vendy index
    url(r'^$', include('vendy.urls')),
    url(r'^vendy/', include('vendy.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)