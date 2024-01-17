from django.urls import path
from .views import *

app_name = 'twitter'

urlpatterns = [
    path('', index_view, name='home'),
    path('form/', form_view, name='form'),
]