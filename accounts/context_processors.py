from .models import Verification
from django.contrib.auth.models import User

def verify(request): 
    answer=0 
    if(request.user.is_authenticated):
        user = request.user
        u = user.username
        try:
            verify=Verification.objects.get(username=u)
            answer=(verify.isSignatureVerified)*(verify.isFaceVerified)
        except Verification.DoesNotExist:
            answer=0
    return {
        'a': answer
    }