from django.contrib import admin
from .models import Category, Author, Product, Review


class CategoryAdmin(admin.ModelAdmin):
    """
    Display the Category model fields in the Admin view
    """
    list_display = ("name",)


class AuthorAdmin(admin.ModelAdmin):
    """
    Display the Author model fields in the Admin view
    """
    list_display = ("name",)


class ProductAdmin(admin.ModelAdmin):
    """
    Display the Product model fields in the Admin view
    """
    list_display = (
        'sku',
        'category',
        'title',
        'author',
        'price',
        'in_stock',
        'image',)

    ordering = ('sku',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'title',
        'content',
        'date',
        'is_featured',
    )

    ordering = ('-date',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
