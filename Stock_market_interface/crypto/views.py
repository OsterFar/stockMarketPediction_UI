from django.shortcuts import render

# Create your views here.
def cryptohomepage(request) :
    return render(request , 'Cryto.html')