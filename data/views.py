from django.shortcuts import render
from django.http import HttpResponse

def teams(request):
    return HttpResponse("Teams Index")