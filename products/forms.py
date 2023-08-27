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


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'