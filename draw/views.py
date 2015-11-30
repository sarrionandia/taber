from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

class DrawControl(View):
    def get(self, request):
        return HttpResponse("OK")