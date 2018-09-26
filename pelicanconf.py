#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'support'
SITENAME = u'SilverOrbit - Philippines DevOps Consultancy'
SITEURL = 'http://blog.silverorbit.com'
SITETITLE = 'SilverOrbit'
SITESUBTITLE = 'Devops | AWS | Consultancy'
SITELOGO = SITEURL + '/images/so_logo.png'

ROBOTS = u'index, follow'

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
LINKS = (("about", "http://www.silverorbit.com/#about"),
         ('contact', 'http://www.silverorbit.com/#contact'),
         ('services', 'http://silverorbit.com/#services'))

#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),)

#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/TeamSilverOrbit'),
          ('facebook','https://www.facebook.com/silverorbit'),
          ('instagram','#'),
          ('github', 'https://github.com/silverorbit'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
('Tags', '/tags.html'),)

COPYRIGHT_YEAR = 2016
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CACHE_CONTENT = False
