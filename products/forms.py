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

    def __init__(self, *args, **kwargs):
        """ Adds placeholders and classes """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Review Title',
            'content': 'Review Content',
        }