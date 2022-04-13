from django.shortcuts import render
import numpy as np
import cv2
from faces import camera
# Create your views here.
def faces(request):
    #print(request.FILES)
    if request.method=='POST' and request.FILES['image_d']:
        return render(request, 'base.html')
    else:
        return render(request, 'faces.html')

def captureimage(request):
    image_d = camera.camera()
    return imread(image_d)
    

