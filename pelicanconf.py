#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from gettext import gettext

AUTHOR = 'admin'
SITENAME = 'گروه کاربران بی‌اس‌دی مشهد'
SITETITLE = 'گروه کاربران بی‌اس‌دی مشهد'
SITESUBTITLE = 'اجتماعی از متخصصین و علاقمندان به سیستم‌عامل‌های مبتنی بر بی‌اس‌دی'
SITEURL = ''
SITELOGO = 'https://upload.wikimedia.org/wikipedia/en/5/55/Bsd_daemon.jpg'
OPENSTREETMAP = 'http://www.openstreetmap.org/export/embed.html?bbox=59.519451856613166%2C36.309254974613616%2C59.53140377998353%2C36.3142952235051&amp;layer=mapnik&amp;marker=36.3117708171057%2C59.52542781829834'

PATH = 'content'

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'fa'
MAIN_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "theme"

USE_FOLDER_AS_CATEGORY = True

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

OG_LOCALE = 'fa'
LOCALE = 'fa'
I18N_TEMPLATES_LANG = 'en'
LOCALE = ('en_US', 'fa_IR')

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']
#JINJA_ENVIRONMENTS = ['jinja2.ext.i18n']
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
I18N_GETTEXT_LOCALEDIR = '/home/gentoo/Projects/web/mashhadbug.org/theme/translations/'
I18N_GETTEXT_DOMAIN = 'messages'

# mapping: language_code -> conf_overrides_dict
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Mashhad BSD User Group',
        'SITETITLE': 'Mashhad BSD User Group',
        'SITESUBTITLE': 'The gathering of local enthusiasts of BSD based Operating Systems',
        'LOCALE': 'en',
        }
    }

# Github Custom Domain
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
