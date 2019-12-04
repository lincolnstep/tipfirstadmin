from django.db import models
from datetime import datetime

# Create your models here.
 
class BusDetail(models.Model):
    code=models.CharField(max_length=50, default=1)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    bustype = models.CharField(max_length=100)
    time=models.TimeField(blank = True,default=datetime.now)
    peak = models.IntegerField(default=0)
    mid = models.IntegerField(default=0)
    off = models.IntegerField(default=0)

    def __str__(self):
        return self.bustype