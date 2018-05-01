from django.contrib import admin
#Make sure to import any new models here.
from .models import Feedback, LocationData, TrailData

#This file pertains to what will show on the admin site.
#Each class will have its own section on the admin site.

class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields' : ['timestamp']}),
        (None,               {'fields' : ['satisfactory_level']}),
        (None,               {'fields' : ['comments']}),
        (None,               {'fields' : ['name']}),
        (None,               {'fields' : ['email']}),
        (None,               {'fields' : ['phone_number']}), 
    ]
    #The line below allows the admin site to display the fields of the model mentioned in the brackets.
    list_display = ('timestamp', 'satisfactory_level', 'comments', 'name', 'email', 'phone_number')
    #The line below allows the admin site to add a filter based on the model fields mentioned in the brackets.
    list_filter = ['timestamp', 'satisfactory_level']
    #The line below allows the admin site to add a search bar that will search based on the models fields mentioned in the brackets.
    search_fields = ['satisfactory_level', 'name', 'email', 'phone_number']


class LocationDataAdmin(admin.ModelAdmin):
    #The reason why 'id' is in the readonly_fields is so that it can not be changed since it is the primary key. Also, it allows the value to be displayed on the admin site.
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
    #The line below allows the admin site to display the fields of the model mentioned in the brackets.
    list_display = ('id', 'picture', 'name', 'latitude', 'longitude', 'hotspot_radius', 'visitor_count', 'hotspot_radius', 'location_type')
    #The line below allows the admin site to add a filter based on the model fields mentioned in the brackets.
    list_filter = ['location_type']
    #The line below allows the admin site to add a search bar that will search based on the models fields mentioned in the brackets.
    search_fields = ['id', 'name', 'latitude', 'longitude', 'hotspot_radius', 'visitor_count', 'hotspot_radius', 'location_type']

class TrailDataAdmin(admin.ModelAdmin):
    #The reason why 'id' is in the readonly_fields is so that it can not be changed since it is the primary key. Also, it allows the value to be displayed on the admin site.
    readonly_fields = ('id',)
    fieldsets = [
        (None,               {'fields' : ['name']}),
        (None,               {'fields' : ['trail_info']}),
        (None,               {'fields' : ['trail_length_in_miles']}),
        (None,               {'fields' : ['trail_latitudes']}),
        (None,               {'fields' : ['trail_longitudes']}),
        (None,               {'fields' : ['trail_type']}),
        (None,               {'fields' : ['trail_color']}),
    ]
    #The line below allows the admin site to display the fields of the model mentioned in the brackets.
    list_display = ('id', 'name', 'trail_info', 'trail_length_in_miles', 'trail_latitudes', 'trail_longitudes', 'trail_type', 'trail_color')
    #The line below allows the admin site to add a filter based on the model fields mentioned in the brackets.
    list_filter = ['trail_type', 'trail_color']
    #The line below allows the admin site to add a search bar that will search based on the models fields mentioned in the brackets.
    search_fields = ['id', 'name', 'trail_length_in_miles', 'trail_type', 'trail_color']

#Here you must regirster each model with the class you made above so the admin site will add it.
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(LocationData, LocationDataAdmin)
admin.site.register(TrailData, TrailDataAdmin)
