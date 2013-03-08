# -*- coding: utf-8 -*-

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pycones.settings")

from django.db.models import signals
from django.db import models


def model_class_prepared(sender, **kwargs):
    """
    Signal fired when a Model subclass has been loaded and processed by the metaclass.

    Here we do several things:
      - Change the definition of 'email', 'last_name' and 'first_name' fields.
    """

    if sender._meta.app_label == 'auth' and sender._meta.module_name == 'user':
        email_field = sender._meta.get_field("email")
        email_field.max_length = 255
        email_field._unique = True

        username = sender._meta.get_field("username")
        username.max_length = 255

        last_name = sender._meta.get_field("last_name")
        last_name.max_length = 255

        first_name = sender._meta.get_field("first_name")
        first_name.max_length = 255


signals.class_prepared.connect(model_class_prepared)
