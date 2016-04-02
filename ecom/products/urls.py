from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url( r'^$',views.ProductListView.as_view(), name='product_list'),
    url(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail')
]
