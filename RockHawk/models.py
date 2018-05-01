import datetime
import os

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


#This file conatins classes that define what a model is and contains. Picture these models as tables you are making in the PostGreSQL database
#NOTE: If you do not define a primary key in the model, PostGreSQL will automatically generate an auto incrementing ID field that will act as the primary key

#This class pertains to the feedback
class Feedback(models.Model) :
    timestamp = models.DateTimeField('date published') #'data published' is just a description of the field
    satisfactory_level = models.IntegerField()
    comments = models.TextField(blank=True) #"blank=True" means the field does not have to contain a value
    name = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone_number = models.TextField(blank=True)
    #Below is to give information about the objects stored in the database when accessed through a terminal
    def __str__(self):
        return '%s %s %s %s %s %s'%(self.timestamp, self.satisfactory_level, self.comments, self.name, self.email, self.phone_number)

#This class pertains to all the landmarks (Activities, Facilities, Hot spots)
class LocationData(models.Model) :
    id = models.AutoField(primary_key=True,)
    picture = models.FileField(blank=True)
    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    hotspot_radius = models.IntegerField()
    visitor_count = models.IntegerField()
    hotspot_info = models.TextField()
    #Below allows you to have a choice of options to choose from on the admin site, you can add choices without dropping the database
    LOCATIONTYPES = (
                    (0, 'Facility'),
                    (1, 'Activity'),
                    (2, 'Hotspot'),
                )
    location_type = models.IntegerField(choices=LOCATIONTYPES) #notice how choices is equal to LOCATIONTYPES
    def __str__(self):
        return '%s %s %s %s %s %s %s %s'%(self.id, self.name, self.latitude, self.longitude, self.hotspot_radius, self.visitor_count, self.hotspot_info, self.location_type)

#This class pertains to all the trails
class TrailData(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.TextField(unique=True)
    trail_info = models.TextField()
    trail_length_in_miles = models.FloatField()
    trail_latitudes = ArrayField(models.FloatField(blank=True))
    trail_longitudes = ArrayField(models.FloatField(blank=True))
    #Below allows you to have a choice of options to choose from on the admin site, you can add choices without dropping the database
    TRAILTYPES = (
                    (0, 'Foot'),
                    (1, 'Biking'),
                    (2, 'Multi-Use'),
                    (3, 'Plant'),
                )
    trail_type = models.IntegerField(choices=TRAILTYPES)
    #Below allows you to have a choice of options to choose from on the admin site, you can add choices without dropping the database
    TRAILCOLORS = (
                    (0, 'Red'),
                    (1, 'Blue'),
                    (2, 'Orange'),
                    (3, 'Green'),
                    (4, 'Yellow'),
                    (5, 'White'),
                )
    trail_color = models.IntegerField(choices=TRAILCOLORS)
    def __str__(self):
        return '%s %s %s %s %s %s %s %s'%(self.id, self.name, self.trail_info, self.trail_length_in_miles, self.trail_latitudes, self.trail_longitudes, self.trail_type, self.trail_color)

