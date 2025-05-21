# wsgi.py
# WSGI configuration file for deploying the Flask app on PythonAnywhere

import sys
import os

# Define the full path to your project directory
project_home = '/home/gabidomiciano/wsaa_project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import the Flask app from server.py
from server import app as application
