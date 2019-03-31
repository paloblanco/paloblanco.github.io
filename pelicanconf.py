#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Palo Blanco'
SITENAME = 'paloblancogames'
SITEURL = ''

PATH = 'content'
THEME = "../pelican-themes/voidy-bootstrap"

STATIC_PATHS = ['images']

TIMEZONE = 'America/Cancun'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# SOCIAL = (('linkedin', 'https://www.linkedin.com/in/username'),
#           ('github', 'https://github.com/username'),
#           ('twitter', 'https://twitter.com/username'),
#           )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITESUBTITLE ='Data science, visualization, and games.'
SITETAG = "paloblanco."

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"

SOCIAL = (('Twitter', 'https://twitter.com/paloblancogames',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/paloblanco',
         'fa fa-github-square fa-fw fa-lg'),
        )