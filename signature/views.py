from django.shortcuts import render
import os
import numpy as np
import skimage
import cv2
#import measure
import metrics 
from django.core.files.images import ImageFile
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.pip
# 
def signVerify(request):
    #print(request.FILES)
    if request.method=='POST' and request.FILES['signature_v']:
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        #print(username)
        originalsignaturename = username + '_sign.jpg'
        #print(originalsignaturename)
        path_to_image = 'media/' + originalsignaturename
        signature_u=InMemoryUploadedFile(open(path_to_image), None, None, None, None, None).read()
        npimg = np.fromstring(signature_u, np.uint8)
        userSignature = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
        #userSignature = InMemoryUploadedFile(open(path_to_image), None, None, None, None, None)
        print(type(userSignature))
        #print(userSignature)
        print(type(request.FILES['signature_v']))
        signature_v = request.FILES['signature_v'].read()
        npimg = np.fromstring(signature_v, np.uint8)
        verifySignature = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
        print(type(verifySignature))
        #print(verifySignature)
        i = cv2.cvtColor(verifySignature,cv2.COLOR_BGR2RGB)
        verifySignature = cv2.resize(cv2.cvtColor(i.copy(),cv2.COLOR_BGR2GRAY),(100,100))
        userSignature = cv2.resize(cv2.cvtColor(userSignature,cv2.COLOR_BGR2GRAY),(100,100))
    
        SSIM_Value = print(metrics.structural_similarity(userSignature,verifySignature))
        print(SSIM_Value)
        return render(request, 'signature.html')
    else:
        print('error')
        print(request)
        #print(request.FILES['signature_v'])
        return render(request, 'signature.html')
