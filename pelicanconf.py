#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Anne Downes'
SITENAME = 'Trainee Project Site'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'pdf']
PAGE_PATHS = ['pages']

THEME = 'theme'
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

BOOTSTRAP_THEME = 'sandstone'
PYGMENTS_STYLE = 'colorful'
FAVICON = 'images/favicon.png'

OUTPUT_PATH = '../output'
TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'En'

ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Physics on the Web', 'http://www.physics.org/'),
     ('Med Phys Links', 'https://www.aapm.org/links/medphys/'),)

SOCIAL = (('Sean_Carrol', 'https://twitter.com/seanmcarroll'),
         ('PyLinac', 'https://github.com/jrkerns/pylinac'),)
# Social widget

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True