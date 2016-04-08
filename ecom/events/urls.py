from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url( r'^$',views.EventListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='detail'),
    url(r'^create/$', views.EventCreateView.as_view(), name='create')
]
