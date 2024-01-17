from django.db import models
from django.contrib.auth.models import User

class Auth(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile/',default='profile/default.jpg')
    def __str__(self):
        return self.author.username
    
class Twitt(models.Model):
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    content = models.TextField()
    count_view = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    #comments
    checked = models.BooleanField(default=True)
    def __str__(self):
        return self.auth.author.username
    
