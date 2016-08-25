#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Kyle Barlow'
SITENAME = u'kylebarlow.com'
SITEURL = ''
RELATIVE_URLS = True
SITEMAP = {'format' : 'xml'}

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
    # ('Beaker Report', 'https://www.beakerreport.com'),
)

# Social widget
SOCIAL = [
    ('Twitter', 'https://twitter.com/kbsci'),
    ('Facebook', 'https://www.facebook.com/kyleabarlow'),
    ('Google-Plus', 'https://plus.google.com/+KyleBarlow'),
    ('Github', 'https://github.com/kylebarlow'),
    ('linkedin', 'https://www.linkedin.com/in/kyleabarlow'),
    ('email', 'mailto:kb@kylebarlow.com'),
]

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

MENUITEMS = [('Science', '/science')]

DISPLAY_PAGES_ON_MENU = True

STATIC_PATHS = [
    'theme/images', 'images',
    'bsg', 'crickettherm', 'android',
    'files',
]

ARTICLE_EXCLUDES = [
    'bsg', 'crickettherm', 'android',
    'files',
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
CATEGORY_SAVE_AS = 'category/{slug}.html'
AUTHOR_SAVE_AS = ''

# Home page
LANDING_PAGE_ABOUT = {
    'title' : "Kyle Barlow",
    'details' : '<p>I am a computational biologist PhD student living in the San Francisco bay area. <A HREF="http://calband.berkeley.edu/">Go bears!</A></p><p>You can contact me securely by using my <A HREF="KyleBarlow_public.asc">GPG public key</A> or via <A HREF="https://keybase.io/kylebarlow">Keybase</A></p><p>Check out my <A HREF="https://github.com/kylebarlow">GitHub profile</A> for the source code for my open source projects.</p>',
}

# Removed: the source code for <A HREF="https://play.google.com/store/apps/details?id=com.kylebarlow.android.crickettherm">CricketTherm</A> and my other open source projects

PROJECTS = [
{
    'name': 'Rosetta',
    'url': 'https://www.rosettacommons.org/',
    'description': 'Scientific software for computational protein structure prediction and design. '
    'I contribute to this project as part of my graduate thesis work.'
},
# {
#     'name': 'Beaker Report',
#     'url': 'https://www.beakerreport.com/',
#     'description': 'Blog covering issues relating to science, law, and public policy.'
# },

# {
#     'name' : 'CricketTherm',
#     'url': 'https://play.google.com/store/apps/details?id=com.kylebarlow.android.crickettherm',
#     'description': 'Android app to estimate outdoors with no network connection based on cricket chirping rate'
# },
]


SITE_LICENSE = u'<a href="https://www.kylebarlow.com">kylebarlow.com</a> by Kyle Barlow is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. <a rel="license" href="https://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a>'
