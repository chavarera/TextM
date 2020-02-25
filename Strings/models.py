from django.db import models

# Create your models here.
class Example(models.Model):
    ex_id = models.AutoField(primary_key=True)
    classs = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    syntax = models.CharField(max_length=1000)
    example = models.CharField(max_length=2000)
    inputs = models.CharField(max_length=3000)
    output = models.CharField(max_length=5000)
