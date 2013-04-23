# -*- coding: utf-8 -*-

import logging
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import loader

logger = logging.getLogger(__name__)


def send_mail_wrapper(subject, template, context, to):
    try:
        email = EmailMessage(
            subject = subject,
            body = loader.render_to_string(template, context),
            from_email = settings.DEFAULT_FROM_EMAIL,
            to = to
        )
        email.send()
    except IOError as ex:
        logger.error(u'No se ha podido enviar la newsletter. Razón:  %s' % (str(ex)))

