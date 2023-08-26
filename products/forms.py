from .models import Review, Category, Product
from django import forms
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    """ 
    Create form based on Review model for users to leave a review 
    """
    class Meta:
        model = Review
        fields = ('title', 'content')
