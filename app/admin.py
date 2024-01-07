from django.contrib import admin
from .models import Auth,Twitt

@admin.register(Auth)
class AuthAdmin(admin.ModelAdmin):
    pass

@admin.register(Twitt)
class TwittAdmin(admin.ModelAdmin):
    pass