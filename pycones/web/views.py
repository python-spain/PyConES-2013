# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from pycones import utils


def home(request):
    """
    View to get the home page
    """
    context = {}

    return render_to_response("web/home.html",
                    context,
                    context_instance=RequestContext(request))


