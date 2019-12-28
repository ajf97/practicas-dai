from django.contrib import admin
from .models import Musician, Album, MusicalGroup

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(MusicalGroup)