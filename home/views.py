from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("It's the home module, and it's no use to access this page")