from django.contrib import admin

# Register your models here.

from .models import Judge, Team, Institution, Speaker

admin.site.register(Team)
admin.site.register(Institution)
admin.site.register(Speaker)
admin.site.register(Judge)
