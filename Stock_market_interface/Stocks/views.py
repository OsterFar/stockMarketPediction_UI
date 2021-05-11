from django.shortcuts import render

# Create your views here.
def homepage(request) :
    print("i m here")
    return render(request , 'Home.html')