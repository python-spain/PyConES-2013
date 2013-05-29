# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from pycones.web.views import home, contact_us, code_of_conduct

urlpatterns = patterns('pycones.web.urls',
    url(r'^contact-us/$', 'contact_us', name='contact_us'),
    url(r'^$', 'home', name='home'),
)

