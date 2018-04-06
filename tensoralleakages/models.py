from django.db import models
from django.urls import reverse

# Create your models here.

class RnnReading(models.Model):
    rnn_name = models.CharField(max_length=200)
    corpus_desc = models.TextField()
    reading_procedure = models.TextField()
    corpus_path = models.CharField(max_length=200)
    fanfic = models.TextField()
    
    def get_absolute_url(self):
        return reverse('rnnreading-detail', kwargs={'rnn_id': self.id})
    
    def __str__(self):
        return self.rnn_name