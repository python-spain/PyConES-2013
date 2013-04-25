from django.conf.urls.defaults import url, patterns

urlpatterns = patterns("pycones.newsletter.views",
    url(r"^suscribe/$", "suscribe_newsletter", name="suscribe_newletter"),
    url(r"^unsuscribe/$", "unsuscribe_newsletter", name="unsuscribe_newsletter"),
    url(r"^latest/$", "latest_newsletter", name="latest_newsletter"),
    url(r"^article/(?P<slug>[\w\d\-]+)/$","article", name="article"),
    url(r"^(?P<uuid>[\w\-\d]+)/$", "newsletter", name="newsletter"),
)
