from django.urls import path
from My_AppTwo import views

urlpatterns = [
    path('', views.users, name="users"),
]
