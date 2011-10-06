import os
import re
from random import choice
from django.core.management.base import NoArgsCommand, CommandError

class Command(NoArgsCommand):
    help = """ Regenerates the SECRET_KEY in conf/base/settings.py """
    def handle_noargs(self, **options):
        directory = os.getcwd()
        settings_path = os.path.join(directory, 'conf', 'base', 'settings.py')
        settings_contents = open(settings_path, 'r').read()
        fp = open(settings_path, 'w')
        secret_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
        settings_contents = re.sub(r"(?<=SECRET_KEY = ')[^']*(?=')", secret_key, settings_contents)
        fp.write(settings_contents)
        fp.close()
