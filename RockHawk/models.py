import datetime

from django.db import models
from django.utils import timezone


class Feedback(models.Model) :
    timestamp = models.DateTimeField('date published')
    satisfactory_level = models.IntegerField()
    comments = models.TextField()
    def __str__(self):
        return '%s %s %s'%(self.timestamp, self.satisfactory_level, self.comments)
    

    class Meta:
        permissions = (
            ('view_feedback', 'View feedback'),
        )

class LocationData(models.Model) :
    name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    hotspotRadius = models.IntegerField()
    visitorCount = models.IntegerField()
    trailInfo = models.TextField()
    def __str__(self):
        return '%s %s %s %s %s %s'%(self.name, self.latitude, self.longitude, self.hotspotRadius, self.visitorCount, self.trailInfo)
