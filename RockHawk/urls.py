from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'RockHawk'
urlpatterns = [
    url('feedback_list/', views.feedback_list, name='feedback_list'),
    url('feedback_detail/(?P<pk>[0-9]+)/$', views.feedback_detail, name='feedback_detail'),
    url('locationData_list/', views.locationData_list, name='locationData_list'),
    url('locationData_detail/(?P<pk>[0-9]+)/$', views.locationData_detail, name='locationData_detail'),
    url('trailData_list/', views.trailData_list, name='trailData_list'),
    url('trailData_detail/(?P<pk>[0-9]+)/$', views.trailData_detail, name='trailData_detail'),
    url(r'^RockHawk/feedback/$', csrf_exempt(views.feedback_list)),
    url(r'^RockHawk/feedback/(?P<pk>[0-9]+)/$', views.feedback_detail),
    url(r'^RockHawk/locationData/$', csrf_exempt(views.locationData_list)),
    url(r'^RockHawk/locationData/(?P<pk>[0-9]+)/$', views.locationData_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
