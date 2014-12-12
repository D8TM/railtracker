#!/opt/python27/bin/python2.7
import sys, os, user

# sys.path.insert(0, "/usr/lib/python2.7")
sys.path.insert(0, "/home/francist/public_html")
sys.path.insert(0, "/home/francist/public_html/devbox")
sys.path.insert(0, "/home/francist/public_html/devbox/railtracker")

# Switch to the directory of your project.
os.chdir("/home/francist/public_html/devbox/railtracker")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "railtracker.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
