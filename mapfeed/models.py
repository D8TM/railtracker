from django.db import models
from fields import ListField

# Create your models here.
class MapCity(models.Model):
   create_date = models.DateTimeField('Date Created', auto_now_add=True)
   city_name = models.CharField(max_length=200)
   rail_name = models.CharField(max_length=200)
   twitter_id = models.CharField(max_length=15, null=True, blank=True)

   def __unicode__(self):
        return self.city_name + " " + self.rail_name

class MapLine(models.Model):
    #Parent map
    map = models.ForeignKey(MapCity)

    #Line name/color/letter/number
    line_name = models.CharField(max_length=200)

    #Line code
    line_code = models.CharField(max_length=2)

    def __unicode__(self):
        return self.line_name

class MapStation(models.Model):
    #Station Name
    station_name = models.CharField(max_length=200)

    #Station Code
    station_code = models.CharField(max_length=3)

    #Latitude and Longitude
    lat = models.DecimalField(max_digits=13, decimal_places=10)
    lon = models.DecimalField(max_digits=13, decimal_places=10)

    #Coordinates for customized map
    x_coord = models.IntegerField(null=True, blank=True)
    y_coord = models.IntegerField(null=True, blank=True)

    #Lines that run through the station
    lines = models.ManyToManyField(MapLine)

    def __unicode__(self):
        return self.station_name

class MapPath(models.Model):
    station_a = models.ForeignKey(MapStation, related_name='path_a')
    station_b = models.ForeignKey(MapStation, related_name='path_b')

    def __unicode__(self):
        return self.station_a + " to " + self.station_b

class Incident(models.Model):
    #Incident date
    incident_date = models.DateTimeField()

    #Free-text description of incident
    description = models.TextField()

    #Incident category
    incident_type = models.CharField(max_length=15)

    #Dictates animation. DEL = delay; ALE = alert
    warning = models.CharField(max_length=3)

    #Stations affected
    stations = models.ManyToManyField(MapStation)

    #Lines affected
    lines = models.ManyToManyField(MapLine)

    def __unicode__(self):
        return self.incident_date + "(" + self.incident_type + ")"
