from django.conf.urls import url
from views import DrawControl

urlpatterns = [
    url(r'^$', DrawControl.as_view(), name='index'),
]