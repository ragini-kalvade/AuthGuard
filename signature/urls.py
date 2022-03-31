from django.urls import path

from . import views

urlpatterns = [
    path('',views.signature, name='signature')
]