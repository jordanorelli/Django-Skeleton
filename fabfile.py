import os
import string
from fabric.api import local, run, env, sudo, cd
from lib.fabric_helpers import *

def run_tests():
    """ Runs the Django test suite as is.  """
    local("./manage.py test")

def uname():
    """ Prints information about the host. """
    run("uname -a")
