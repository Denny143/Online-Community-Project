"""flamenco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from calender import views as calender_views
from django.contrib.auth import views as auth_views
from calender.views import TeacherCreate,StudioUserCreate,StudioDayView
from calender.views import home,schedules,studios,signup



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', calender_views.home, name='home'),
    url(r'^teachers/$', TeacherCreate.as_view(), name='teacher-add'),
    url(r'^studiousers/$', StudioUserCreate.as_view(), name='studio_user-add'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', StudioDayView.as_view(month_format='%m'),name="studio_daily_schedule"),
    url(r'^studio_calendar/$', calender_views.studios, name='studios'),
    #url(r'^studios/$',StudioView.as_view(),name='studios'),
    url(r'^signup/$', calender_views.signup, name='signup'),
    #url(r'^studioform/$',studioform.as_view(), name='studioform'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
]
