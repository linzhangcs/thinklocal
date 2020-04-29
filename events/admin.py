from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "ThinkLocal Admin"
admin.site.site_title = "ThinkLocal Admin"
admin.site.index_title = "Welcome to ThinkLocal Admin Page"

admin.site.register(Event)
admin.site.register(Attendee)
