from django.contrib import admin

from .models import Choice, Question, Student

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

admin.site.register(Question, QuestionAdmin)
admin.site.register(Student, StudentAdmin)
