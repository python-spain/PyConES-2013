# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from pycones import utils
from pycones.sponsors.models import Sponsor

def home(request):
    """
    View to get the home page
    """
    context = {
        'diamonds': Sponsor.objects.filter(level='diamond'),
        'platinums': Sponsor.objects.filter(level='platinum'),
        'golds': Sponsor.objects.filter(level='gold'),
        'silvers': Sponsor.objects.filter(level='silver'),
    }

    return render_to_response("web/home.html",
                    context,
                    context_instance=RequestContext(request))


