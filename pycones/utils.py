# -*- coding: utf-8 -*-

import logging
from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template import loader

logger = logging.getLogger(__name__)


def mail_wrapper(subject, context, from_email, to, template_txt, template_html=None):
    try:
        email = EmailMultiAlternatives(
            subject = subject,
            body = loader.render_to_string(template_txt, context),
            from_email = from_email,
            to = to
        )
        if template_html:
            html_body = loader.render_to_string(template_html, context)
            email.attach_alternative(html_body, 'text/html')
            email.content_subtype = 'html'
        return email
    except IOError as ex:
        logger.error(u'Error en utils.mail_wrapper: %s' % (str(ex)))

