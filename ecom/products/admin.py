from django.contrib import admin

from .models import Product, Variation, ProductImage, Category, ProductFeatured

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0
    max_num = 5


class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price']
    inlines = [
        ProductImageInline,
        VariationInline,
    ]
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(Variation)

admin.site.register(ProductImage)

admin.site.register(Category)

admin.site.register(ProductFeatured)
