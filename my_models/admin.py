from django.contrib import admin
from .models import Person, Runner, User_Profile,Publisher,Book,Author

admin.site.register([Person, Runner, User_Profile, Publisher, Book, Author])

admin.site.site_header='Dataflair Django Site'