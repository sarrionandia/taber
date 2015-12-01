from django.http import HttpResponse
from django.views.generic import View


class DrawTableView(View):

    def get(self, request, round):
        return HttpResponse("OK")