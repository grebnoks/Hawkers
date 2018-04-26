"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('locationData_list/', include('RockHawk.urls')),
    path('feedback_list/', include('RockHawk.urls')),
    path('admin/', admin.site.urls),
    url('', admin.site.urls),
    url(r'^', include('RockHawk.urls')),
    url(r'^RockHawk/', include('RockHawk.urls')),
    url('admin/password/change/$', 
        auth_views.PasswordChangeView.as_view(), 
        name='password_change'),
    url('admin/password/change/done/$',
        auth_views.PasswordChangeDoneView.as_view(), 
        name='password_change_done'),
    url('admin/password/reset/$', 
        auth_views.PasswordResetView.as_view(), 
        name='password_reset'),
    url('admin/password/reset/done/$', 
        auth_views.PasswordResetDoneView.as_view(), 
        name='password_reset_done'),
    url('admin/password/reset/\
        (?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        auth_views.PasswordResetConfirmView.as_view(), 
        name='password_reset_confirm'),
    url('admin/password/reset/complete/$', 
        auth_views.PasswordResetCompleteView.as_view(), 
        name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

