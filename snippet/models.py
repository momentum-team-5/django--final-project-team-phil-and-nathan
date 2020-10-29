from django.db import models
from users.models import User

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    # language = models.CharField(max_length=255)
    # copied_snippet = models.ManyToManyField("self")
    # author = models.ForeignKey User, null=True, on_delete=models.CASCADE

