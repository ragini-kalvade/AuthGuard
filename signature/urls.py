from django.urls import path

from . import views

urlpatterns = [
    path('signVerify',views.signVerify, name='signVerify')
]