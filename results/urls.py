from django.conf.urls import url

from results.views import EditResultsView, ResultsTableView, CurrentResultsTableView

urlpatterns = [
        url(r'^$', CurrentResultsTableView.as_view(), name='current_result'),
        url(r'^edit/(?P<debateid>\d+)/$', EditResultsView.as_view(), name='edit_results'),
        url(r'^round/(?P<round>\d+)/$', ResultsTableView.as_view(), name='results_table'),
]