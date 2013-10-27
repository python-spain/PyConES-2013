# -*- coding: utf-8 -*-

import json

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from django import http

from pycones import utils
from pycones.sponsors.models import Sponsor
from pycones.call4papers.models import Talk, SC_TRACK, SC_DAY, SC_HOUR


def home(request):
    """
    View to get the home page
    """
    talks = {}
    for sc_track in SC_TRACK:
        for sc_day in SC_DAY:
            for sc_hour in SC_HOUR:
                slot = sc_track[0] + sc_day[0] + sc_hour[0]
                try:
                    talk = Talk.objects.get(slot=slot, selected=True)
                    talks.update({
                        slot:render_to_string('web/talk.html', {'talk':talk})
                    })
                except:
                    pass
    context = {
        'diamonds': Sponsor.objects.filter(level='diamond').order_by("?"),
        'platinums': Sponsor.objects.filter(level='platinum').order_by("?"),
        'golds': Sponsor.objects.filter(level='gold').order_by("?"),
        'silvers': Sponsor.objects.filter(level='silver').order_by("?"),
        'bronce': Sponsor.objects.filter(level='bronce').order_by("?"),
        'talks': talks,
    }

    return render_to_response("web/home.html", context,
                              context_instance=RequestContext(request))


def contact_us(request):
    """
    View to send an email to organization
    """

    if request.method != 'POST':
        return redirect('/')

    name = request.POST.get('name', None)
    contact_email = request.POST.get('contact_email', None)
    message = request.POST.get('message', None)

    if not name or not contact_email or not message:
        context = {'message': u'Rellena todos los campos'}
        return http.HttpResponseBadRequest(json.dumps(context),
                                           content_type="application/json")

    body = u"{0}\n{1}".format(contact_email, message)
    send_mail(u'Contacto a través de formulario web', body, contact_email,
              ['contacto2013@es.pycon.org'], fail_silently=False)

    context = {'message': u'Mensaje enviado. Muchas gracias'}
    return http.HttpResponse(json.dumps(context), content_type="application/json")
