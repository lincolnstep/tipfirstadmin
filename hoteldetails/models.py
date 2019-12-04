from django.db import models



# Create your models here.
class HotelDetail(models.Model):
    location = models.CharField(max_length=200,blank=False)
    category = models.CharField(max_length=300,blank=False)
    hoteltype = models.IntegerField(default=1,blank=False)
    hotelname = models.CharField(max_length=100,blank=False)
    mealplan = models.CharField(max_length=20,blank=False)
    pax = models.FloatField(blank=False,default=2)
    peak = models.IntegerField(blank=False)
    mid = models.IntegerField(blank=False)
    off = models.IntegerField(blank=False)
    bitly = models.CharField(blank=False,max_length=50,default='')

    def __str__(self):
        return self.hotelname