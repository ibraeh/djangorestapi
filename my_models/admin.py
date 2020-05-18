from django.contrib import admin
from .models import Person, Runner, User_Profile

admin.site.register([Person, Runner, User_Profile])

