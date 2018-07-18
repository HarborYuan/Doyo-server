from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=200)
    token = models.CharField(max_length=200)

    def __str__(self):
        return self.username
