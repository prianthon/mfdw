from django.conf.urls import url

from . import views
from .views import QuoteList

urlpatterns = [
    url(r'^$', views.quote_req, name='quote-request'),
    url(r'show$', QuoteList.as_view(), name='show-quotes'),
]
