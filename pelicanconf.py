#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'support'
SITENAME = u'SilverOrbit'
SITEURL = 'http://localhost:8000'
SITETITLE = 'SilverOrbit'
SITESUBTITLE = 'Devops | AWS | BigData'
SITELOGO = SITEURL + '/images/planet-earth.png'

PATH = 'content'

TIMEZONE = 'Asia/Manila'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('about', 'http://www.silverorbit.com/#about'),
         ('contact', 'http://www.silverorbit.com/#contact'),
         ('services', ''))

#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', '#'),
          ('facebook','#'),
          ('instagram','#'),
          ('github', 'https://github.com/silverorbit'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
('Tags', '/tags.html'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
