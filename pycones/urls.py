from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.views.generic.simple import direct_to_template
#Changes 1.5
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

from rest_framework.routers import DefaultRouter
from pycones.call4papers.api import TalkViewSet, SpeakerViewSet
from pycones.sponsors.api import SponsorViewSet

api_router = DefaultRouter()
api_router.register('talks', TalkViewSet)
api_router.register('speakers', SpeakerViewSet)
api_router.register('sponsors', SponsorViewSet)


urlpatterns = patterns("",
    url(r"^", include('pycones.web.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^api/v1/", include(api_router.urls)),
    url(r"^newsletter/", include("pycones.newsletter.urls", namespace="newsletter")),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)

def mediafiles_urlpatterns():
    """
    Method for serve media files with runserver.
    """

    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]

    from django.views.static import serve
    return patterns('',
        (r'^%s(?P<path>.*)$' % _media_url, serve,
            {'document_root': settings.MEDIA_ROOT})
    )


# This only works on development mode
urlpatterns += staticfiles_urlpatterns()
urlpatterns += mediafiles_urlpatterns()
