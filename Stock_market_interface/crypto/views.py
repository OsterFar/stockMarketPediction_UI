from django.shortcuts import render

# Create your views here.
def cryptohomepage(request) :
    return render(request , 'CrytoMain.html')



def cryptoPrimary(request) :
    print("hello world")
    return render(request , "Cryto.html")