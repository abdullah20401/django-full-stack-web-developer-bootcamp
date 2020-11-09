from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bye/', views.bye, name='bye'),
]
