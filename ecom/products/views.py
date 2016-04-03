from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__contains=query) |
                Q(description__contains=query)
            )
            return qs


class ProductDetailView(DetailView):
    model = Product

