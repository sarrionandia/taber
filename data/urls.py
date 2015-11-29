from django.conf.urls import url

from . import views
from views import DeleteInstitutionView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^institution/(?P<institutionid>\d+)/$', DeleteInstitutionView.as_view(), name="delete_institution"),
]
