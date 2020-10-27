from django.db import models
from users.models import User
# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField()
    copies = models.ManyToMany(Snippet)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

