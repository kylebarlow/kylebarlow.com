#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Kyle Barlow'
SITENAME = u'Kyle Barlow'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Beaker Report', 'http://www.beakerreport.com'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/kbsci'),
    ('Facebook', 'https://www.facebook.com/kyleabarlow'),
    ('Google-Plus', 'https://plus.google.com/+KyleBarlow'),
    ('Github', 'https://github.com/kylebarlow'),
)

DEFAULT_PAGINATION = 10

THEME = 'pelican-elegant'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'filetime_from_git']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
IGNORE_FILES = ['.#*']

STATIC_PATHS = [
    'theme/images', 'images',
    'bsg', 'crickettherm', 'android',
]

ARTICLE_EXCLUDES = [
    'bsg', 'crickettherm', 'android',
]

EXTRA_PATH_METADATA = {}

static_dir = 'static_root'
# All files in static will be placed at root level (must be files)
for f in os.listdir( os.path.join(PATH, static_dir) ):
    fpath = os.path.join(static_dir, f)
    STATIC_PATHS.append(fpath)
    EXTRA_PATH_METADATA[fpath] = { 'path' : f }
    ARTICLE_EXCLUDES.append(fpath)

TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Home page
LANDING_PAGE_ABOUT = {
    'title' :'This is my landing page about',
    'details' : '<p>My name is Kyle Barlow and I am a computational biologist living in the beautiful San Francisco bay area (not pictured, so take my word for it). <A HREF="http://calband.berkeley.edu/">Go bears!</A></p><p>You can contact me at <A HREF="mailto:kb@kylebarlow.com">kb@kylebarlow.com</A> (my GPG public key is <A HREF="KyleBarlow_public.asc">here)</A> or find me at <A HREF="http://www.linkedin.com/in/kyleabarlow">LinkedIn</A> or on <a href="http://plus.google.com/106160593415513011050?prsrc=3" rel="publisher">Google+</A>.</p><p>Check out my <A HREF="https://github.com/kylebarlow">GitHub profile</A> for the source code for <A HREF="https://play.google.com/store/apps/details?id=com.kylebarlow.android.crickettherm">CricketTherm</A> and my other open source projects.</p>',
}

PROJECTS = [
{
    'name': 'Logpad + Duration',
    'url': 'https://github.com/talha131/logpad-plus-duration#logpad--duration',
    'description': 'Vim plugin to emulate Windows Notepad logging feature,'
    ' and log duration of each entry'
},
{
    'name': 'Elegant Theme for Pelican',
    'url': 'http://oncrashreboot.com/pelican-elegant',
    'description': 'A clean and distraction free theme, with search and a'
    ' lot more unique features, using Jinja2 and Bootstrap'
},
]
