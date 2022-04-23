from django.shortcuts import render
from PIL import Image
import numpy as np
import cv2
import os 
from . import views
import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.core.mail import EmailMessage
from faces import face_recognizer
from faces import faces_train
import glob
import shutil
import os
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading


def faces(request):
    
    #print(request.FILES)
    if request.method=='POST':
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        
        originalPhoto = username + '_photo.jpg'
        path_to_image = './' + 'media\\' + originalPhoto
        src_dir = path_to_image
        #print(path_to_image)

        userPhoto = cv2.imread(path_to_image)
        directory = username
        dir_path = 'C:/Users/HP/Documents/SignatureRecognition/faces/FaceDetectionModel/images/'
        path = os.path.join(dir_path,directory)
        dst_dir = path+'.jpg'
        #print(dst_dir)

        if (os.path.isdir(path)== False):
            os.mkdir(path)
        for jpgfile in glob.iglob(src_dir):
            shutil.copy(jpgfile, path)
        
        faces_train.train_faces()
        
        return render(request, 'base.html')
    
    else:
        return render(request, 'faces.html') 

    

