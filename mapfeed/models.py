from django.db import models
from fields import ListField

# Create your models here.
class MapCity(models.Model):
   create_date = models.DateTimeField('Date Created')
   city_name = models.CharField(max_length=200)
   rail_name = models.CharField(max_length=200)

   def __unicode__(self):
        return self.city_name + " " + self.rail_name

class MapStation(models.Model):
    station_name = models.CharField(max_length=200)
    status = models.IntegerField()
    status_tweet = models.CharField(max_length=140)
    x_coord = models.IntegerField()
    y_coord = models.IntegerField()

    def __unicode__(self):
        return self.station_name

class MapLine(models.Model):
    map = models.ForeignKey(MapCity)
    line_name = models.CharField(max_length=200)
    status = models.IntegerField()
    reverse_status = models.IntegerField()
    status_tweet = models.CharField(max_length=140)
    reverse_tweet = models.CharField(max_length=140)
    #stations = ListField()

    def __unicode__(self):
        return self.line_name

class MapPath(models.Model):
    station_a = models.ForeignKey(MapStation, related_name='path_a')
    station_b = models.ForeignKey(MapStation, related_name='path_b')

    def __unicode__(self):
        return self.station_a + " to " + self.station_b

#class Feed(models.Model):
#    def __unicode__(self):
#        return '-'
