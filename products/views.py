from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from .forms import ReviewForm


# Create your views here.

def all_products(request):
    """ 
    A view to show all products, including sorting and search queries 
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show individual product details and any reviews left by users
    """
    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.all().order_by("-date")

    context = {
        'product': product,
        'review': review,
        'review_form': ReviewForm()
    }

    return render(request, 'products/product_detail.html', context)

