from django.shortcuts import render
from .FunctionDictt import callFunction_object
# Create your views here.
def homepage(request) :
    dictt = callFunction_object()
    #dictt = 0
    
    return render(request , 'Home.html',{'content':dictt})