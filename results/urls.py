from django.conf.urls import url

from results.views import EditResultsView

urlpatterns = [
        url(r'^edit/(?P<debateid>\d+)/$', EditResultsView.as_view(), name='edit_results'),
]