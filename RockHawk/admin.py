from django.contrib import admin

from .models import Feedback, LocationData


class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['timestamp']}),
        (None,               {'fields': ['satisfactory_level']}),
        (None,               {'fields' : ['comments']}),
    ]
    list_display = ('timestamp', 'satisfactory_level', 'comments')
    list_filter = ['timestamp']
    search_fields = ['satisfactory_level']


class LocationDataAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['latitude']}),
        (None,               {'fields': ['longitude']}),
        (None,               {'fields': ['hotspotRadius']}),
        (None,               {'fields': ['visitorCount']}),
        (None,               {'fields': ['trailInfo']}),
        (None,               {'fields': ['locationType']}),
    ]
    list_display = ('id', 'name', 'latitude', 'longitude', 'hotspotRadius', 'visitorCount', 'trailInfo', 'locationType')
    search_fields = ['id', 'name', 'latitude', 'longitude', 'hotspotRadius', 'visitorCount', 'trailInfo', 'locationType']

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(LocationData, LocationDataAdmin)
