# -*- coding: utf-8 -*-

import uuid
import json

from django.contrib.sites.models import Site
from django.conf import settings
from django.core import mail
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.db import transaction
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

from pycones import utils
from .models import Subscription, Newsletter, Article


def _make_static_url():
    return 'http://{0}{1}'.format(
                        Site.objects.get_current(),
                        settings.STATIC_URL)


def _make_unsubscribe_url(user_email, val_token):
    url = reverse('newsletter:unsubscribe_newsletter')
    current_site = Site.objects.get_current()

    return 'http://{0}{1}?user_email={2}&val_token={3}'.format(
                current_site.domain, url, user_email, val_token)


def send_welcome_msg(user_email, val_token, request):
    subject = u'¡Bienvenido a PyConES!'
    from_email = u'boletin2013@es.pycon.org'

    context = {
        "user_email": user_email,
        "val_token": val_token,
        "unsubscribe_url": _make_unsubscribe_url(user_email, val_token)
    }

    template_txt = 'newsletter/newsletter_welcome_mail.txt'
    template_html =  'newsletter/newsletter_welcome_mail.html'
    to = [user_email]

    email = utils.mail_wrapper(subject, context, from_email, to, template_txt, template_html)
    email.send()


@transaction.commit_on_success
def subscribe_newsletter(request):
    """
    View to subscribe new users to newsletter
    """
    if request.method != 'POST':
        return redirect('/')

    user_email = request.POST.get('user_email', None)
    if not user_email:
        context = {'message' : u"Error al recoger el email. Inténtalo de nuevo más tarde"}
        return HttpResponseBadRequest(json.dumps(context),
                                      content_type="application/json")

    subscription_queryset = Subscription.objects.filter(user_email=user_email)

    try:
        subscription = subscription_queryset.get()
        context = {'message' : u"Se ha producido un error. Quizás ya estés dado de alta."}
        return HttpResponseBadRequest(json.dumps(context), content_type="application/json")
    except Subscription.DoesNotExist:
        subscription = Subscription(user_email=user_email, val_token=str(uuid.uuid4()))
        subscription.save()

    send_welcome_msg(subscription.user_email, subscription.val_token, request)

    context = {'message' : u"Registrado. Muchas gracias"}
    return HttpResponse(json.dumps(context), content_type="application/json")


def unsubscribe_newsletter(request):
    """
    View to unsubscribe newsletter
    """
    if request.method != 'GET':
        return redirect('/')

    user_email = request.GET.get('user_email', None)
    val_token = request.GET.get('val_token', None)

    if not user_email or not val_token:
        context = {"message": u"Parámetros incorrectos"}
        return render_to_response("newsletter/unsubscribe.html", context,
                                  context_instance=RequestContext(request))

    queryset = Subscription.objects.filter(user_email=user_email, val_token=val_token)
    try:
        subscription = queryset.get()
    except Subscription.DoesNotExist:
        context = {"message": u"Usuario no encontrado."}
    else:
        subscription.delete()
        context = {"message": u"Eliminado de la newsletter correctamente"}

    return render_to_response("newsletter/unsubscribe.html", context,
                              context_instance=RequestContext(request))


def latest_newsletter(request):
    """
    View to get latest newsletter
    """
    try:
        newsletter = Newsletter.objects.filter(sent=True).order_by('-sent_date')[:1][0]
    except:
        return HttpResponseRedirect('/')

    context = {
        "newsletter": newsletter,
        "static_url": _make_static_url()
    }

    return render_to_response("newsletter/newsletter.html", context,
                              context_instance=RequestContext(request))


def newsletter(request, uuid):
    """
    View to get newsletter by uuid
    """
    newsletter = get_object_or_404(Newsletter, uuid=uuid)
    context = {
        "newsletter": newsletter,
        "static_url": _make_static_url()
    }

    return render_to_response("newsletter/newsletter.html", context,
                              context_instance=RequestContext(request))


def article(request, slug):
    """
    View to get article by slug
    """
    article = get_object_or_404(Article, slug=slug)

    return render_to_response("newsletter/article.html", {"article": article},
                              context_instance=RequestContext(request))

