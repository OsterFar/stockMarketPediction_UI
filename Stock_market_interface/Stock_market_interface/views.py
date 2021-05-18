
from django.http.response import JsonResponse
from django.shortcuts import render
import requests
import json

def refresh(request) :
    print("Jee=============")
    dataa = "Hello world"
    return JsonResponse(dataa)
