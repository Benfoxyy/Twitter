from django.db import models
from django.contrib.auth.models import User
    
class Twitt(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    count_view = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    #comments
    checked = models.BooleanField(default=True)
    def __str__(self):
        return self.auth.username
    
