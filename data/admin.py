from django.contrib import admin

from .models import Judge, Team, Institution, Speaker, Venue

admin.site.register(Team)
admin.site.register(Institution)
admin.site.register(Speaker)
admin.site.register(Judge)
admin.site.register(Venue)
