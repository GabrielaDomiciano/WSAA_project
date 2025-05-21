import sys
import os
from server import app as application

project_home = '/home/gabidomiciano/wsaa_project'
if project_home not in sys.path:
    sys.path.insert(0, project_home)
