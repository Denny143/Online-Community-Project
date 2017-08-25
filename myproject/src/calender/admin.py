from django.contrib import admin

# Register your models here.

from .models import studio_calendar,user_calendar

admin.site.register(studio_calendar)

admin.site.register(user_calendar)
