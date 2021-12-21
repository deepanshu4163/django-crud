from django.contrib import admin
from .models import Person

#to reflect our Person model in admin page
admin.site.register(Person)

