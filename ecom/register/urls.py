from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url( r'^new/(?P<pk>\d+)/$',views.RegisterCreateView.as_view(), name='new'),
    url(r'^thanks/(?P<pk>\d+)/$', views.thanks, name='thanks')
    #url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail')
]
