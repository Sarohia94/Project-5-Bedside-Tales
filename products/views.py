from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Review, Category
from .forms import ReviewForm


def all_products(request):
    """ 
    A view to show all products, including sorting and search queries 
    """
    products = Product.objects.all()

    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = Product.objects.get(pk=product_id)
            review.user = request.user
            review.save()
            messages.success(request, "Review added!")
            return redirect('product_detail', product_id=product_id)
        else:
            messages.error(request,'Error in form')
    
    return render(request, 'products/product_detail.html', context)
