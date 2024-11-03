from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexed_body, name = 'indexed_body'),
    path('get-location/', views.get_location, name = 'get_location'),
]
