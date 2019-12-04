from django.db import models


# Create your models here.

class CabDetail(models.Model):
    type_of_cab =models.CharField(max_length=20,blank=False,default='cab')
    pickup = models.CharField(max_length=200,blank=False)
    destination = models.CharField(max_length=200,blank=False)
    drop = models.CharField(max_length=200,blank=False)
    cabname=models.CharField(max_length=20,blank=False)
    category = models.CharField(max_length=100,blank=False)
    capacity = models.IntegerField(default=4,blank=False)
    peak = models.IntegerField(blank=False)
    mid = models.IntegerField(blank=False)
    off = models.IntegerField(blank=False)

    def __str__(self):
        return self.type_of_cab