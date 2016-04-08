from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     context["query"] = self.request.GET.get("q")
    #     return context


    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(title__contains=query) |
                Q(description__contains=query)
            )
            return qs
        return qs


class ProductDetailView(DetailView):
    model = Product

