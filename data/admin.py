from django.contrib import admin

from .models import Judge, Team, Institution, Venue

admin.site.register(Team)
admin.site.register(Institution)
admin.site.register(Judge)
admin.site.register(Venue)
