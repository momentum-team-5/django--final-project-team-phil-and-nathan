from django.db import models
# from django.conf import settings
# User = settings.AUTH_USER_MODEL
from users.models import User



class Snippet(models.Model):
    """Represent a code snippet"""
    title = models.CharField(max_length=255, blank = True, null = True)
    body = models.TextField()
    language = models.CharField(max_length=255) 
    copied_snippet = models.ManyToManyField("self", blank = True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='snippets')



    


