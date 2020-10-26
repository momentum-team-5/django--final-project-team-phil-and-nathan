from django.db import models

class Snippet(models.Model):
    """Represent a code snippet"""
    title = models.CharField(max_length=255, blank = True, null = True)
    body = models.TextField()
    language = models.CharField(max_length=255) 
    #author = models.ForeignKey(User, on_delete=Cascade)
    #original_author = models.ForeignKey(Snippet, ??????)

    


