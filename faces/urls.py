from django.urls import path
from . import views

urlpatterns = [
    path('faces', views.faces, name='faces'),
    path('captureimage',views.captureimage, name='captureimage') 
]