from django.urls import path
from django.conf.urls import url
from polls import views
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    url(r'^polls/student/$', views.student_list),
    url(r'^polls/student/(?P<pk>[0-9]+)/$', views.student_detail),
    url(r'^polls/feedback/$', views.feedback_list),
    url(r'^polls/feedback/(?P<pk>[0-9]+)/$', views.feedback_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
