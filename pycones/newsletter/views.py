# -*- coding: utf-8 -*-

import uuid

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.db import transaction
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from .models import Subscription, Newsletter, Article


def send_welcome_msg(email_user, token, request):
    from django.core.mail import EmailMultiAlternatives

    subject = u'¡Bienvenido a PyConES!'
    from_email = u'boletin2013@es.pycon.org'

    context = {"email": email_user, "token": token}
    context_email = {'email_user' : email_user, 'token' : token}

    text_content = render_to_string("newsletter_welcome_mail.txt", context,
                                    context_instance=RequestContext(request))
    html_content = render_to_string("newsletter_welcome_mail.html", context,
                                    context_instance=RequestContext(request))

    msg = EmailMultiAlternatives(subject, text_content, from_email, [email_user])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@transaction.commit_on_success
def suscribe_newsletter(request):
    """
    View to suscribe new users to newsletter
    """

    if request.method != 'POST':
        return redirect('/')

    email = request.POST.get('email_user', None)

    if not email:
        context = {'message' : u"Error al recoger el email. Inténtalo de nuevo mas tarde"}
        return render_to_response("newsletter/comingsoon_message.html", context,
                                  context_instance=RequestContext(request))

    subscription_queryset = Subscription.objects.filter(user_email=email)

    try:
        subscription = subscription_queryset.get()
        context = {'message' : u"Se ha producido un error. Quizás ya estes dado de alta."}
        return render_to_response("newsletter/comingsoon_message.html",
                                context,
                                context_instance=RequestContext(request))
    except Subscription.DoesNotExist:
        subscription = Subscription(user_email=email, val_token=str(uuid.uuid4()))
        subscription.save()

    send_welcome_msg(subscription.user_email, subscription.val_token, request)

    context = {'message' : u"Registrado. Muchas gracias"}
    return render_to_response("newsletter/comingsoon_message.html", context,
                               context_instance=RequestContext(request))


def unsuscribe_newsletter(request):
    """
    View to unsuscribe newsletter
    """
    if request.method != 'GET':
        return redirect('/')

    email = request.GET.get('email', None)
    token = request.GET.get('val_token', None)

    if not email or not token:
        context = {"message": u"Parámetros incorrectos"}
        return render_to_response("newsletter/comingsoon_message.html",
                        context, context_instance=RequestContext(request))

    queryset = Subscription.objects.filter(user_email=email, val_token=token)
    try:
        subscription = queryset.get()
    except Subscription.DoesNotExist:
        context = {"message": u"Usuario no encontrado."}
    else:
        subscription.delete()
        context = {"message": u"Eliminado de la newsletter correctamente"}

    return render_to_response("newsletter/comingsoon_message.html",
                        context, context_instance=RequestContext(request))

def latest_newsletter(request):
    """
    View to get latest newsletter
    """
    try:
        newsletter = Newsletter.objects.all().order_by('-sent_date')[:1][0]
    except:
        return HttpResponseRedirect('/')

    return render_to_response("newsletter/newsletter.html",
                    {"newsletter": newsletter},
                    context_instance=RequestContext(request))

def newsletter(request, uuid):
    """
    View to get newsletter by uuid
    """
    newsletter = get_object_or_404(Newsletter, uuid=uuid)

    return render_to_response("newsletter/newsletter.html",
                    {"newsletter": newsletter},
                    context_instance=RequestContext(request))


def article(request, slug):
    """
    View to get article by slug
    """
    article = get_object_or_404(Article, slug=slug)

    return render_to_response("newsletter/article.html",
                    {"article": article},
                    context_instance=RequestContext(request))


