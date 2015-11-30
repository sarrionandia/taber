from django.conf.urls import url
from views import DrawControl, DrawFirstRound

urlpatterns = [
    url(r'^$', DrawControl.as_view(), name='index'),
    url(r'^round/first/$', DrawFirstRound.as_view(), name="drawround")
]