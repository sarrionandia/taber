from django.conf.urls import url

from . import views
from views import DeleteInstitutionView, CreateInstitutionView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^institution/(?P<institutionid>\d+)/delete/$', DeleteInstitutionView.as_view(), name="delete_institution"),
    url(r'^institution/create/$', CreateInstitutionView.as_view(), name="create_institution"),
]
