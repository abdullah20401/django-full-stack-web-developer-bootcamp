from django.urls import path, include
from Challenge_App import views

urlpatterns = [
    path('', views.help,name='help'),
]
