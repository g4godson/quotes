from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),

    url(r'^home$', views.home ),
    url(r'^add$', views.add ),
    url(r'^(?P<id>\d+)/like$', views.like ),
    url(r'^(?P<id>\d+)/delete$', views.delete ),
    url(r'^(?P<id>\d+)/edit$', views.edit ),
    url(r'^(?P<id>\d+)/update$', views.update ),
    url(r'^(?P<id>\d+)/show$', views.show ),
]
