from django.db import models
from fields import ListField, ColourField

# Create your models here.
class MapCity(models.Model):
   #Creation date
   create_date = models.DateTimeField('Date Created', auto_now_add=True)

   #Name of the city
   city_name = models.CharField(max_length=200)

   #Local rail name
   rail_name = models.CharField(max_length=200)

   #Twitter screen name
   twitter_id = models.CharField(max_length=15, null=True, blank=True)

   class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

   def __unicode__(self):
        return self.city_name + " " + self.rail_name

class MapLine(models.Model):
    #Parent map
    map = models.ForeignKey(MapCity)

    #Line name/color/letter/number
    line_name = models.CharField(max_length=200)

    #Line code
    line_code = models.CharField(max_length=2)

    #Line color
    #color = ColourField()
    color = models.CharField(max_length=6)

    def __unicode__(self):
        return self.line_name

    class Meta:
        verbose_name = 'Line'
        verbose_name_plural = 'Lines'

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

    #Repeat stations. Typically, the intersection of two lines
    through_station = models.ForeignKey('self', null=True)

    def __unicode__(self):
        return self.station_name

    class Meta:
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'

class MapPath(models.Model):
    #Line associated with path
    line = models.ForeignKey(MapLine)

    #Station info
    station = models.ForeignKey(MapStation)

    #Sequence in the line
    seq_num = models.IntegerField()

    class Meta:
        verbose_name = 'Path'
        verbose_name_plural = 'Paths'

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
        #return self.incident_date.strftime("%Y-%m-%d %H:%M:%S") + "(" + self.incident_type + ")"
        return self.incident_type

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'

class Dict_Entry(models.Model):
    #Dictionary key
    lookup = models.CharField(max_length=140)

    #Dictionary value (ie category/line/station)
    translation = models.CharField(max_length=140)

    #Translation category (line/station/incident category)
    CAT_CHOICES = (
            ('IC', 'Incident Category'),
            ('ST', 'Station'),
            ('LI', 'Line'),
    )
    translation_cat = models.CharField(max_length=2, choices=CAT_CHOICES)

    #Associated cities
    city = models.ManyToManyField(MapCity)

    def __unicode__(self):
        return self.lookup

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
