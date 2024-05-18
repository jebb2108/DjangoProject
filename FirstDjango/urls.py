from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.get_info),
]
