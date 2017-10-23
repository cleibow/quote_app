from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^quotes/new$', views.newQuote),
    url(r'^$', views.index)
]
