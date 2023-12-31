from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
from .models import Featured


def contact_us(request, *args, **kwargs):
    """
    Contact us view for users
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for contacting us! We will get back to you soon.'
                )
            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'Error in submitting form, please ensure the form is valid.'
                )
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()

    return render(request, 'other/contact_us.html', {'form': form})


def featured_author(request):
    """
    A page on a promoted/featured author of the month
    """

    featured = Featured.objects.filter(is_featured=True)

    context = {
        'featured_author': featured
    }

    return render(request, 'other/featured_author.html', context)
