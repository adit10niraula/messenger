from django.contrib import admin

from .models import Profile, Friends, Message
# Register your models here.

admin.site.register([Profile,Friends,Message])