from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    names = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank =True)
    friend = models.ManyToManyField('Friends')

    def __str__(self):
        return self.names


class Friends(models.Model):
    friend = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.friend.names




class Message(models.Model):
    body = models.CharField(max_length=200)
    msg_send = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="send")
    msg_recive = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recieve")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body