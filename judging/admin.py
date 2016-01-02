from django.contrib import admin

from judging.forms import PanelForm
from judging.models import Panel

class PanelAdmin(admin.ModelAdmin):
    form = PanelForm

admin.site.register(Panel, PanelAdmin)