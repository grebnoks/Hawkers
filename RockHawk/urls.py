from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'RockHawk'
urlpatterns = [
    url(r'^RockHawk/feedback/$', views.feedback_list),
    url(r'^RockHawk/feedback/(?P<pk>[0-9]+)/$', views.feedback_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
