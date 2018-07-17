from django.db import models

class Users(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username