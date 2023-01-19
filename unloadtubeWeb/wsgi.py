"""
WSGI config for unloadtubeWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unloadtubeWeb.settings')

application = get_wsgi_application()

# import os, sys

# sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR']))

# os.environ['DJANGO_SETTINGS_MODULE'] = 'unloadtubeWeb.settings'

# virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'

# os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages')

# virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
# try:
#     exec(virtualenv, dict(__file__=virtualenv))
# except IOError:
#     pass

# #
# # IMPORTANT: Put any additional includes below this line.  If placed above this
# # line, it's possible required libraries won't be in your searchable path
# #

# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()