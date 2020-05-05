from django.urls import path, re_path
from BasicApp import views

# TEMPLATE TAGGING
app_name = 'BasicApp'

urlpatterns = [
    re_path(r'^relative/$', views.relative, name='relative'),
    re_path(r'^other/$', views.other, name='other'),
]