from django.db import models
from products.models import Product, Author


class Contact(models.Model):
    """
    Contact Form model
    """
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    date = models.DateField(auto_now_add=True, blank=False, null=False)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=2000)

    class Meta:
        ordering = ['-date']


class Featured(models.Model):
    """
    A model for the featured author of the month
    """

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author_image_url = models.URLField(max_length=1500, null=True, blank=True)
    author_image = models.ImageField(null=False, blank=False)
    about = models.TextField()
    website_url = models.URLField(max_length=1500, null=True, blank=True)
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['author']

    def __str__(self):
        return f"Featured author {self.author}"
