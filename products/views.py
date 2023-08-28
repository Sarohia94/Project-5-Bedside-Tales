from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Review, Category
from .forms import ReviewForm, ProductForm, AuthorForm


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
    A view to show individual product details and 
    to add and view reviews left by users
    """

    product = get_object_or_404(Product, pk=product_id)
    review = Review.objects.filter(product=product_id).order_by("-date")

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


@login_required
def add_product(request):
    """ 
    Add a product to the store 
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_author(request):
    """
    Add an Author to the store 
    """

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":

        form = AuthorForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added a new Author!")
            return redirect(reverse("add_product"))
        else:
            messages.error(
                request, "Failed to add a new Author. \
                    Please check if the form is valid."
            )
    else:
        form = AuthorForm()
    
    template = "products/add_author.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ 
    Edit a product in the store 
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ 
    Delete a product from the store 
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    
    return redirect(reverse('products'))