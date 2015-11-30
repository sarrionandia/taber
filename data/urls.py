from django.conf.urls import url

from . import views
from views import DeleteInstitutionView, CreateInstitutionView, UpdateInstitutionView, DeleteTeamView, CreateTeamView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^institution/(?P<institutionid>\d+)/delete/$', DeleteInstitutionView.as_view(), name="delete_institution"),
    url(r'^institution/create/$', CreateInstitutionView.as_view(), name="create_institution"),
    url(r'^institution/(?P<institutionid>\d+)/update/$', UpdateInstitutionView.as_view(), name='update_institution'),
    url(r'^team/(?P<teamid>\d+)/delete/$', DeleteTeamView.as_view(), name='delete_team'),
    url(r'^team/create/$', CreateTeamView.as_view(), name='create_team'),
]
