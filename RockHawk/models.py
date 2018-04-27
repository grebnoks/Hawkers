import datetime
import os

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class Feedback(models.Model) :
    timestamp = models.DateTimeField('date published')
    satisfactory_level = models.IntegerField()
    comments = models.TextField(blank=True)
    name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone_number = models.TextField(blank=True)
    def __str__(self):
        return '%s %s %s %s %s %s'%(self.timestamp, self.satisfactory_level, self.comments, self.name, self.email, self.phone_number)
    

    class Meta:
        permissions = (
            ('view_feedback', 'View feedback'),
        )



class LocationData(models.Model) :
    id = models.AutoField(primary_key=True,)
    picture = models.FileField(upload_to=settings.MEDIA_ROOT, blank=True)
    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    hotspot_radius = models.IntegerField()
    visitor_count = models.IntegerField()
    hotspot_info = models.TextField()
    LOCATIONTYPES = (
                    (0, 'Facility'),
                    (1, 'Activity'),
                    (2, 'Hotspot'),
                )
    location_type = models.IntegerField(choices=LOCATIONTYPES)
    def __str__(self):
        return '%s %s %s %s %s %s %s %s'%(self.id, self.name, self.latitude, self.longitude, self.hotspot_radius, self.visitor_count, self.hotspot_info, self.location_type)

class TrailData(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    trail_info = models.TextField()
    trail_length_in_miles = models.FloatField()
    trail_latitudes = ArrayField(models.FloatField(blank=True))
    trail_longitudes = ArrayField(models.FloatField(blank=True))
    TRAILTYPES = (
                    (0, 'Foot'),
                    (1, 'Biking'),
                    (2, 'Multi-Use'),
                    (3, 'Plant'),
                )
    trail_type = models.IntegerField(choices=TRAILTYPES)
    def __str__(self):
        return '%s %s %s %s %s %s %s'%(self.id, self.name, self.trail_info, self.trail_length_in_miles, self.trail_latitudes, self.trail_longitudes, self.trail_type)

