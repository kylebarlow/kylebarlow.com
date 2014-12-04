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

GOOGLE_ANALYTICS = u'UA-20247595-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

RESPONSIVE_IMAGES = True
FIGURE_NUMBERS = True

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
    ('linkedin', 'https://www.linkedin.com/in/kyleabarlow'),
    ('email', 'mailto:kb@kylebarlow.com'),
)

DEFAULT_PAGINATION = 10

THEME = 'pelican-elegant'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = [
    'sitemap', 'extract_toc', 'tipue_search', 'filetime_from_git',
    'better_figures_and_images',
    'optimize_images',
]
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
    'title' : "Kyle Barlow's Homepage",
    'details' : '<p>My name is Kyle Barlow and I am a computational biologist PhD student living in the San Francisco bay area. <A HREF="http://calband.berkeley.edu/">Go bears!</A></p><p>You can contact me using my <A HREF="KyleBarlow_public.asc">GPG public key.</A></p><p>Check out my <A HREF="https://github.com/kylebarlow">GitHub profile</A> for the source code for <A HREF="https://play.google.com/store/apps/details?id=com.kylebarlow.android.crickettherm">CricketTherm</A> and my other open source projects.</p>',
}

PROJECTS = [
{
    'name' : 'CricketTherm',
    'url': 'https://play.google.com/store/apps/details?id=com.kylebarlow.android.crickettherm',
    'description': 'Android app to estimate outdoors with no network connection based on cricket chirping rate'
},
{
    'name': 'Rosetta',
    'url': 'https://www.rosettacommons.org/',
    'description': 'Scientific software for computational protein structure prediction and design. '
    'I contribute to this project as part of my graduate work.'
},
{
    'name': 'Beaker Report',
    'url': 'http://www.beakerreport.com/',
    'description': 'Blog covering issues relating to science, law, and public policy.'
},
]
