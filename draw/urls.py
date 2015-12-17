from django.conf.urls import url
from views import DrawControl, DrawFirstRound, DrawNextRound

urlpatterns = [
    url(r'^$', DrawControl.as_view(), name='index'),
    url(r'^round/first/$', DrawFirstRound.as_view(), name="drawround"),
    url(r'^next/$', DrawNextRound.as_view(), name='drawnext')
]