from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

