from django.shortcuts import render

# Create your views here.

def signature(request):
    return render(request, 'signature.html')