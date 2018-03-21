from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
    
class SyntaxToxen(models.Model):
    token_str = models.CharField(max_length=200)
    terminal = models.BooleanField
    
class ConstituencyRule(models.Model):
    token_in = models.ForeignKey(SyntaxToxen, on_delete=models.CASCADE, related_name="token_in")
    left_out = models.ForeignKey(SyntaxToxen, on_delete=models.CASCADE, related_name="left_out")
    right_out = models.ForeignKey(SyntaxToxen, on_delete=models.CASCADE, related_name="right_out")
    
class TerminalRule(models.Model):
    cat_in = models.ForeignKey(SyntaxToxen, on_delete=models.CASCADE, related_name="cat_in")
    terminal_out = models.ForeignKey(SyntaxToxen, on_delete=models.CASCADE, related_name="terminal_out") #Should be terminal, unenforced
    
    