from django.contrib import admin
from .models import *

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('user','title','created', 'published')


admin.site.register(Photo, PhotoAdmin)