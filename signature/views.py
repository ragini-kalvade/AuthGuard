from django.shortcuts import render, redirect
import os
import numpy as np
import skimage
import cv2
import metrics 
from django.contrib import messages
from accounts.models import Verification

def remove_white_space(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (25,25), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    noise_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, noise_kernel, iterations=2)
    close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, close_kernel, iterations=3)
    #Find enclosing boundingbox and crop ROI\n”,
    coords = cv2.findNonZero(close)
    x,y,w,h = cv2.boundingRect(coords)
    return image[y:y+h, x:x+w]

def signVerify(request):
    #print(request.FILES)
    if request.method=='POST' and request.FILES['signature_v']:
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        
        originalsignaturename = username + '_sign.jpg'
        path_to_image = './' + 'media\\' + originalsignaturename
        #print(path_to_image)

        userSignature = cv2.imread(path_to_image)
      
        signature_v = request.FILES['signature_v'].read()
        npimg = np.fromstring(signature_v, np.uint8)
        verifySignature = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)

        #print(verifySignature)
        i = cv2.cvtColor(verifySignature,cv2.COLOR_BGR2RGB)
        verifySignature = cv2.resize(cv2.cvtColor(i.copy(),cv2.COLOR_BGR2GRAY),(400,200))
        userSignature = cv2.resize(cv2.cvtColor(userSignature,cv2.COLOR_BGR2GRAY),(400,200))
    
        SSIM_Value = skimage.metrics.structural_similarity(userSignature,verifySignature)
        
        if(SSIM_Value < 0.75):
            answer = 'Signature not matched'
        else:  
            answer = 'Signature matched'
            verify=Verification.objects.get(username=username)
            verify.isSignatureVerified=1
            verify.save()
        messages.info(request, answer)
        return render(request, 'signature.html')
    else:
        return render(request, 'signature.html')
