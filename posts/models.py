from datetime import datetime
from distutils.command.upload import upload
import email
from email.policy import default
from tkinter import CASCADE
import django
from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=100, default='')
    # slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to='images/', default='', blank=True)
    details = models.CharField(max_length=1000000,default='')
    created_date = models.DateTimeField(default=datetime.now, blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    body = models.TextField(max_length=10000)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return 'Comment {} by {} - {}'.format(self.body, self.name, self.created_date)
