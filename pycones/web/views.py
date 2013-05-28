# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.utils import simplejson as json

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
        return HttpResponseBadRequest(json.dumps(context),
                                      content_type="application/json")

    body = contact_email + '\n' + message
    send_mail(u'Contacto a través de formulario web', body, contact_email,
        ['contacto2013@es.pycon.org'], fail_silently=False)

    context = {'message': u'Mensaje enviado. Muchas gracias'}
    return HttpResponse(json.dumps(context), content_type="application/json")
