from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist


def wishlist(request):
    """ 
    A view to show the user's wishlist 
    Requests login and displays error message
    """

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user_profile=user)

    if not request.user.is_authenticated:
        messages.error(request,
                       'Please log in to access your Wishlist.')
        return redirect(reverse('account_login'))

    template = 'wishlist/wishlist.html'

    context = {
        'wishlist': wishlist
    }

    return render(request, template, context)


def add_to_wishlist(request, product_id):
    """
    Add to wishlist view 
    Requests login and displays error message
    Prevents from adding same book twice
    Success message for new book added
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_authenticated:
        messages.error(request,
                       'Please log in to add to your Wishlist.')
        return redirect(reverse('account_login'))

    already_added = Wishlist.objects.filter(product=product,
                                       user_profile=user).exists()
    if already_added:
        messages.info(request, f'{product.title} is already in your Wishlist!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        wishlist_book = Wishlist.objects.create(user_profile=user,
                                                product=product)
    messages.success(request,
                     f'{product.title} has been added to your Wishlist!')

    return redirect(reverse('product_detail', args=[product.id]))
