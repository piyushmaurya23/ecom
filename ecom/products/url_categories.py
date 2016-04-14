from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url( r'^$', views.CategoryListView.as_view(), name='list'),
    url(r'^new/$', views.CategoryCreateView.as_view(), name='create'),
    #url(r'^image/$', views.ImageCreateView.as_view(), name='upload'),
    url(r'^(?P<slug>[\w-]+)/$', views.CategoryDetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/inventory/$', views.VariationListView.as_view(), name='inventory'),
]
