# -*- coding: utf-8 -*-
# Django settings for account project

import os
import posixpath
from django.utils.translation import ugettext_lazy as _

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = True

ADMINS = (
    ("Yamila Moreno", "yamila.ms@gmail.com"),
    ("Alberto Chamorro", "a.chamorro.ruiz@gmail.com"),
)

DATABASES = {
   "default": {
      "ENGINE": "django.db.backends.postgresql_psycopg2", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
      "NAME": "",                       # Or path to database file if using sqlite3.
      "USER": "",                             # Not used with sqlite3.
      "PASSWORD": "",                         # Not used with sqlite3.
      "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
      "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
   }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/Madrid"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "es"

LANGUAGES = (
    ('ca', _(u'Català')),
    ('eu', _(u'Euskara')),
    ('es', _(u'Español')),
    ('ga', _(u'Galego')),
    ('en', _(u'English')),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, "locale"),
    )

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PACKAGE_ROOT, "static"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv(
    'SECRET_KEY', "8*br)9@fs!4nzg-imfrsst&oa2udy6z-fqtdk0*e5c1=wn)(t3")

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.transaction.TransactionMiddleware",
]


TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
]

ROOT_URLCONF = "pycones.urls"

TEMPLATE_DIRS = [
    os.path.join(PACKAGE_ROOT, "templates"),
]

INSTALLED_APPS = (
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # external
    "debug_toolbar",
    "south",
    "rosetta",
    "rest_framework",

    # pycones
    "pycones.newsletter",
    "pycones.web",
    "pycones.sponsors",
    "pycones.call4papers",
)

# Debug toolbar
if DEBUG:
    MIDDLEWARE_CLASSES.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    DEBUG_TOOLBAR_CONFIG = {
        "INTERCEPT_REDIRECTS": False,
    }


# Rosetta settings
ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'es'
ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = u'Español'
ROSETTA_STORAGE_CLASS = 'rosetta.storage.SessionRosettaStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass

