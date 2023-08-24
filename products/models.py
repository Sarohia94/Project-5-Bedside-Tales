from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    A model to allocate Categories to the books
    """
    name = models.CharField(max_length=254)

    class Meta:
        """
        Direct the admin how to display the plural of the Category model
        """
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    A model to define an author
    """
    name = models.CharField(max_length=254, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A model to define the book products
    """
    category = models.ForeignKey("Category", null=True, blank=True, 
                                    on_delete=models.SET_NULL
                                    )
    sku = models.CharField(max_length=250, null=True, blank=True, unique=True)
    title = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    goodreads_url = models.URLField(max_length=1500, null=True, blank=True)
    description = models.TextField()
    image_url = models.URLField(max_length=1500, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    A model for users to leave a book review
    """
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=500)
    # automatically create and add date when a review is added
    date = models.DateField(auto_now_add=True, blank=False, null=False)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
