from django.db import models
from django.urls import reverse

# Create your models here.
    
class Lsystem(models.Model):
    """ Model for an L-system, including initial text. """
    init_text = models.TextField()
    
    def __str__(self):
        return self.init_text
    
    def get_absolute_url(self):
        return reverse('apruning', kwargs={'lsystem_id': self.id})

class Lrule(models.Model):
    """ Model for a rule in an L-system, consisting of a list of input string and a list of output strings."""
    str_in = models.CharField(max_length=200)
    str_out = models.CharField(max_length=200)
    rule_priority = models.IntegerField(default=0)
    lsys = models.ForeignKey(Lsystem, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return ('{} -> {}'.format(self.str_in, self.str_out))