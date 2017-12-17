# restaurantes/urls.py

from django.conf.urls import url, include
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^home/$', views.index),
  url(r'^register/$', views.register),
  url(r'^restaurants/$', views.restaurants),
  url(r'^contact/$', views.contact),
  url(r'^search/$', views.search),
  url(r'^search-ajax/$', views.search_ajax)
]
