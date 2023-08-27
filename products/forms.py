from .models import Review, Category, Product, Author
from django import forms
from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    """ 
    Create form based on Review model for users to leave a review 
    """
    class Meta:
        model = Review
        fields = ('title', 'content')


class ProductForm(forms.ModelForm):
    """
    Superuser can use Product Form to manage book admin
    """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Override the init() method to make changes to some fields
        """
        super().__init__(*args, **kwargs)


class AuthorForm(forms.ModelForm):
    """
    Superuser Author Form to manage adding new author
    """

    class Meta:
        model = Author
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)