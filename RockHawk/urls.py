from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

#This file pertains to all the urls that the software can access.

app_name = 'RockHawk'
urlpatterns = [
    url('feedback_list/', views.feedback_list, name='feedback_list'), #This is the API url where GET, POST, and PUT requests can be made to for a list of all the feeback responses
    url('feedback_detail/(?P<pk>[0-9]+)/$', views.feedback_detail, name='feedback_detail'), #This is the API url where GET, POST, and PUT requests can be made to specific feedback responses.
    url('locationData_list/', views.locationData_list, name='locationData_list'), #This is the API url where GET, POST, and PUT requests can be made to for a list of all the location data responses
    url('locationData_detail/(?P<pk>[0-9]+)/$', views.locationData_detail, name='locationData_detail'), #This is the API url where GET, POST, and PUT requests can be made to specific location data responses.
    url('trailData_list/', views.trailData_list, name='trailData_list'), #This is the API url where GET, POST, and PUT requests can be made to for a list of all the trail data responses
    url('trailData_detail/(?P<pk>[0-9]+)/$', views.trailData_detail, name='trailData_detail'), #This is the API url where GET, POST, and PUT requests can be made to specific trail responses.
    #The url's below pertain to the web pages on the admin site, each of the pairs will handle either displaying the entire list or displaying specific records.
    url(r'^RockHawk/feedback/$', views.feedback_list),
    url(r'^RockHawk/feedback/(?P<pk>[0-9]+)/$', views.feedback_detail),
    url(r'^RockHawk/locationData/$', views.locationData_list),
    url(r'^RockHawk/locationData/(?P<pk>[0-9]+)/$', views.locationData_detail),
    url(r'^RockHawk/trailData/$', views.locationData_list),
    url(r'^RockHawk/trailData/(?P<pk>[0-9]+)/$', views.locationData_detail),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
