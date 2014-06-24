# -*- coding:utf-8 -*-

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "18efe6c9-2430-48ab-a656-fc5983cdcce2354b4575-1b4b-46d0-97ae-70ac419be439ebcc7771-9c01-4a95-b3c0-f9a757a66ce7"
NEVERCACHE_KEY = "bfe26cda-75bf-4c5b-b7cd-85be601222f75aa9c632-4618-42fb-b1c9-d48a8bdaa65bc556a0cc-b865-4e7c-b9d1-99374d5352c3"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# add by weiguobin

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    # "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.pages",
    # "mezzanine.galleries",
    # "mezzanine.twitter",
    "mezzanine.accounts",
    "mezzanine.mobile",

    # "debug_toolbar",
)

USE_I18N = True

ALLOWED_HOSTS = ['']

LANGUAGE_CODE = 'zh-cn'
# LANGUAGE_CODE = 'en'



TIME_ZONE = 'Asia/Shanghai'

DEFAULT_CHARSET='utf-8'

a=u'中国人'