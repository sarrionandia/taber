from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


class EditResultsView(View):

    def get(self, request, debateid):
        return HttpResponse("OK")

