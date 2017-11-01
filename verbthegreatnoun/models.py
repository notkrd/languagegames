from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class WordDoes(models.Model):
    the_word = models.CharField("word", max_length=100, primary_key=True)
    meaning = models.TextField
    synonyms = ArrayField

class VerbDoes(WordDoes):
    action = models.TextField("code for action")  # Should be Python code. I know this is dangerous, but I like flying in to the sun's hot breath etc.

class NameDoes(WordDoes):
    attributes = models.CharField

class NounPhraseDoes(WordDoes):
    noun_type = models.CharField(max_length=100)
    individuals = models.ManyToManyField(NameDoes)
    capabilities = models.TextField("verbs a subject knows")
    
class LocationDoes(NounPhraseDoes):
    exits = models.ManyToManyField("self")
    names_in = models.ManyToManyField(NameDoes)