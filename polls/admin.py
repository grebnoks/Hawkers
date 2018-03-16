from django.contrib import admin

from .models import Choice, Question, Student, Feedback, LocationBasedData

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['major']}),
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['age']}),
    ]
    list_display = ('major', 'name', 'age')
    search_fields = ['major', 'name', 'age']

class FeedbackAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['timestamp']}),
        (None,               {'fields': ['satisfactory_level']}),
        (None,               {'fields' : ['comments']}),
    ]
    list_display = ('timestamp', 'satisfactory_level', 'comments')
    list_filter = ['timestamp']
    search_fields = ['satisfactory_level']

class LocationBasedDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['latitude']}),
        (None,               {'fields': ['longitude']}),
        (None,               {'fields': ['hotspotRadius']}),
        (None,               {'fields': ['visitorCount']}),
        (None,               {'fields': ['trailInfo']}),
    ]
    list_display = ('latitude', 'longitude', 'hotspotRadius', 'visitorCount', 'trailInfo')
    search_fields = ['latitude', 'longitude', 'hotspotRadius', 'visitorCount', 'trailInfo']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(LocationBasedData, LocationBasedDataAdmin)
