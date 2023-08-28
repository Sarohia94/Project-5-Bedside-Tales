from django.db import models


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