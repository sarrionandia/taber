from django.conf.urls import url

from results.views import EditResultsView, ResultsTableView

urlpatterns = [
        url(r'^edit/(?P<debateid>\d+)/$', EditResultsView.as_view(), name='edit_results'),
        url(r'^round/(?P<round>\d+)/$', ResultsTableView.as_view(), name='results_table'),
]