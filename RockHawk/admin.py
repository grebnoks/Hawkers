from django.contrib import admin

from .models import Feedback, LocationData, TrailData
#from PIL import Image


class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields' : ['timestamp']}),
        (None,               {'fields' : ['satisfactory_level']}),
        (None,               {'fields' : ['comments']}),
        (None,               {'fields' : ['name']}),
        (None,               {'fields' : ['email']}),
        (None,               {'fields' : ['phone_number']}), 
    ]
    list_display = ('timestamp', 'satisfactory_level', 'comments', 'name', 'email', 'phone_number')
    list_filter = ['timestamp', 'satisfactory_level']
    search_fields = ['satisfactory_level', 'name', 'email', 'phone_number']


class LocationDataAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        (None,               {'fields' : ['picture']}),
        (None,               {'fields' : ['name']}),
        (None,               {'fields' : ['latitude']}),
        (None,               {'fields' : ['longitude']}),
        (None,               {'fields' : ['hotspot_radius']}),
        (None,               {'fields' : ['visitor_count']}),
        (None,               {'fields' : ['hotspot_info']}),
        (None,               {'fields' : ['location_type']}),
    ]
    list_display = ('id', 'picture', 'name', 'latitude', 'longitude', 'hotspot_radius', 'visitor_count', 'hotspot_radius', 'location_type')
    list_filter = ['location_type']
    search_fields = ['id', 'name', 'latitude', 'longitude', 'hotspot_radius', 'visitor_count', 'hotspot_radius', 'location_type']

class TrailDataAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        (None,               {'fields' : ['name']}),
        (None,               {'fields' : ['trail_info']}),
        (None,               {'fields' : ['trail_length_in_miles']}),
        (None,               {'fields' : ['trail_latitudes']}),
        (None,               {'fields' : ['trail_longitudes']}),
        (None,               {'fields' : ['trail_type']}),
    ]
    list_display = ('id', 'name', 'trail_info', 'trail_length_in_miles', 'trail_latitudes', 'trail_longitudes', 'trail_type')
    list_filter = ['trail_type']
    search_fields = ['id', 'name', 'trail_length_in_miles', 'trail_type']

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(LocationData, LocationDataAdmin)
admin.site.register(TrailData, TrailDataAdmin)
