from django.conf.urls.defaults import url, patterns

urlpatterns = patterns("pycones.newsletter.views",
    url(r"^subscribe/$", "subscribe_newsletter", name="subscribe_newsletter"),
    url(r"^unsubscribe/$", "unsubscribe_newsletter", name="unsubscribe_newsletter"),
    url(r"^latest/$", "latest_newsletter", name="latest_newsletter"),
    url(r"^article/(?P<slug>[\w\-\d]+)/$","article", name="article"),
    url(r"^(?P<uuid>[\w\-\d]+)/$", "newsletter", name="newsletter"),
)
