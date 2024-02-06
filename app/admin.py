from django.contrib import admin
from .models import Twitt

@admin.register(Twitt)
class TwittAdmin(admin.ModelAdmin):
    pass