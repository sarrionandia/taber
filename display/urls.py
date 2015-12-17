from django.conf.urls import url

from views import DrawTableView, TeamStandingView

urlpatterns = [
        url(r'^table/(?P<round>\d+)/$', DrawTableView.as_view(), name='update_institution'),
        url(r'^standing/team/$', TeamStandingView.as_view(), name='team_standings'),
]