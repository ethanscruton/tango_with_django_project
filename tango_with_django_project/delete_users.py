import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User

for user in User.objects.all():
    if user.username != 'ethan':
        user.delete()
    