from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def FirstView(request):
    return HttpResponse('Working on Docker Container')
