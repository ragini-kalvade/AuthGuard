from django.urls import path
from . import views

urlpatterns = [
    # path('faces_train',views.faces_train,name='faces_train'),
    # path('face_recognizer',views.face_recognizer, name='face_recognizer'),
    path('faces', views.faces, name='faces'),
]