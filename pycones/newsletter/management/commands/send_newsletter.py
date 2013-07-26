# -*- coding: utf-8 -*-

from django.core import mail
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.conf import settings

from pycones.newsletter.models import *
from pycones import utils

class Command(BaseCommand):

    args = ''
    help = 'Send newsletter'
    sd = None

    def send_newsletter(self):
        #SEND NEWSLETTER
        newsletter = Newsletter.objects.filter(sent=False).order_by('-created_date')[0]

        emails = []
        subject = '[PyConES] %s' % newsletter.title
        context = {
            'newsletter': newsletter,
            'mail': True
        }
        from_email = settings.EMAIL_HOST_USER
        template_txt = 'newsletter/newsletter.txt'
        template_html = 'newsletter/newsletter.html'

        subscribers = Subscription.objects.all()
        if settings.EMAIL_DEBUG:
            subscribers = subscribers.filter(admin=True)

        for subscriber in subscribers:
            to = [subscriber.user_email]
            current_site = Site.objects.get_current()
            context['unsubscribe_url'] = 'http://%s%s?user_email=%s&val_token=%s' % (current_site.domain, reverse('newsletter:unsubscribe_newsletter'), subscriber.user_email, subscriber.val_token)
            context['static_url'] = 'http://%s%s' % (current_site.domain, settings.STATIC_URL)
            email = utils.mail_wrapper(subject, context, from_email, to, template_txt, template_html)
            emails.append(email)

        connection = mail.get_connection(fail_silently=True)
        connection.send_messages(emails)

        if not settings.EMAIL_DEBUG:
            newsletter.sent = True
            newsletter.save()


    def handle(self, *args, **options):
        print "Sending newsletter"
        self.send_newsletter()
        print "All sent ok"
