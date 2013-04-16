# -*- coding: utf-8 -*-

import uuid

from django.shortcuts import render_to_response,redirect
from django.db import transaction
from django.template.loader import render_to_string
from django.template import RequestContext
from django import http

from .models import Subscription,Newsletter,Article


def send_welcome_msg(email_user, token):
    from django.core.mail import EmailMultiAlternatives

    subject = u'¡Bienvenido a PyConES!'
    from_email = u'boletin2013@es.pycon.org'

    context = {"email": email_user, "token": token}
    context_email = {'email_user' : email_user, 'token' : token}

    text_content = render_to_string("newsletter_welcome_mail.txt", context)
    html_content = render_to_string("newsletter_welcome_mail.html", context)

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
        context = {'message' : u"Error al recoger el email. Intentalo de nuevo mas tarde"}
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

    send_welcome_msg(subscription.user_email, subscription.val_token)

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
        context = {"message": u"Parametros incorrectos"}
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

def get_last_newsletter(request):
    """
    View to get latest newsletter
    """
    newsletter = Newsletter.objects.get_latest_newsletter()

    return render_to_response("newsletter/newsletter.html",
                    {"newsletter":newsletter},
                    context_instance=RequestContext(request))

def get_newsletter(request,year_month):
    """
    View to get newsletter by date
    """
    year=year_month[:4]
    month=year_month[-2:]
    newsletter = Newsletter.objects.get_newsletter(year,month)

    return render_to_response("newsletter/newsletter.html",
                    {"newsletter":newsletter},
                    context_instance=RequestContext(request))

def send_newsletter(request,year_month):
    """
    View to send a newsletter by email
    """
    pass

def get_article(request,article_path):
    """
    View to get article by path
    """
    article = Article.objects.get_article_by_path(article_path)

    return render_to_response("newsletter/article.html",
                    {"article":article},
                    context_instance=RequestContext(request))


