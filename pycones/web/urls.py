# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from pycones.web.views import home

urlpatterns = patterns('pycones.web.urls',
    url(r'^$', 'home', name='home'),
)
