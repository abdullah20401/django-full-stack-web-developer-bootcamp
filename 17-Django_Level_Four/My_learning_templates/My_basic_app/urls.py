from django.urls import path
from My_basic_app import views

# TEMPLATE TAGGING
app_name = 'My_basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
