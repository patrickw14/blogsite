from django.db import models

class Post(models.Model):
    blogPost = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    wasEdited = models.BooleanField()
    dateEdited = models.DateTimeField('date edited')
