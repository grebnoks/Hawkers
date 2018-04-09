from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'RockHawk'
urlpatterns = [
    url('feedback_list/', views.feedback_list, name='feedback_list'),
    url('locationData_list/', views.locationData_list, name='locationData_list'),
    url(r'^RockHawk/feedback/$', csrf_exempt(views.feedback_list)),
    url(r'^RockHawk/feedback/(?P<pk>[0-9]+)/$', views.feedback_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
