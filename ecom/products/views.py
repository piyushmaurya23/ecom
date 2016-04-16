from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

import random

from .forms import VariationInventoryFormSet
from .models import Product, Variation, ProductImage, Category, ProductFeatured


def home(request):
    featured_image = ProductFeatured.objects.first()
    context = {
        "featured_image": featured_image
    }

    return render(request, "products/home.html", context)

class CategoryListView(ListView):
    model = Category
    queryset = Category.objects.all()


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        obj = self.get_object()
        product_set  = obj.product_set.all()
        default_products = obj.default_category.all()
        products = ( product_set | default_products ).distinct()
        context["products"] = products
        return context



class CategoryCreateView(CreateView):
    model = Category
    fields = [
        'title',
        'slug',
        'description',
    ]


class VariationListView(LoginRequiredMixin, ListView):
    model = Variation
    queryset = Variation.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(VariationListView, self).get_context_data(*args, **kwargs)
        context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset())
        return context

    def get_queryset(self, *args, **kwargs):
        product_pk = self.kwargs.get("pk")
        if product_pk:
            product = get_object_or_404(Product, pk=product_pk)
            queryset = Variation.objects.filter(product=product)
        return queryset

    def post(self, request, *args, **kwargs):
        formset = VariationInventoryFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                new_item = form.save(commit=False)
                product_pk = self.kwargs.get("pk")
                product = get_object_or_404(Product, pk=product_pk)
                new_item.product = product
                new_item.save
            messages.success(request, "Inventory and price successfully updated")
            return redirect("products:list")


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

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        instance = self.get_object()
        context["related"] = sorted(Product.objects.get_related(instance)[:6], key=lambda x: random.random())
        return context



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = [
        'title',
        'description',
        'price',
        'active',
    ]


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = ProductImage
    fields = [
        'product',
        'image',
    ]
