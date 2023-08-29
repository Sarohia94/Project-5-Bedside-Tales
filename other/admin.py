from django.contrib import admin
from .models import Contact, Featured


class ContactAdmin(admin.ModelAdmin):
    """
    Contact us info displayed in admin
    """
    list_display = (
        'name',
        'email',
        'date',
        'subject',
        'message',
    )

    ordering = ('-date',)


class FeaturedAdmin(admin.ModelAdmin):
    """
    Featured author fields displayed in admin
    """
    list_display = (
        'author',
        'website_url',
        'product',
        'is_featured'
    )

    ordering = ('-author',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Featured, FeaturedAdmin)
