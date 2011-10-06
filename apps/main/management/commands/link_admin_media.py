from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib import admin
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        admin_media_path = os.path.join(os.path.dirname(admin.__file__),
                                        'media')
        print "Admin media: " + admin_media_path
