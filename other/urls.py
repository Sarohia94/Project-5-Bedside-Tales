from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.contact_us, name='contact_us'),
    path('featured/', views.featured_author, name='featured_author'),
]