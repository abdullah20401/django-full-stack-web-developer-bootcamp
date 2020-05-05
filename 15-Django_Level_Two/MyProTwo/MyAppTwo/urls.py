from django.urls import path, include
from MyAppTwo import views

urlpatterns = [
    path('',views.index,name='index')
]
