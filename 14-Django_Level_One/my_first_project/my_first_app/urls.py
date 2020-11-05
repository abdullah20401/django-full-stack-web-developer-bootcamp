from django.urls import path
from my_first_app import views

urlpatterns = [
    path('', views.index, name="index"),
]