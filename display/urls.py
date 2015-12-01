from django.conf.urls import url

from views import DrawTableView

urlpatterns = [
        url(r'^table/(?P<round>\d+)/$', DrawTableView.as_view(), name='update_institution'),
]