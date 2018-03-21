from django.db import models
from django.urls import reverse

# Create your models here.

class JustText(models.Model):
    txt = models.TextField()
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=200, default="")
    
    def get_absolute_url(self):
        return reverse('read-text', kwargs={'txt_id': self.id})
    
    def __str__(self):
        return self.title