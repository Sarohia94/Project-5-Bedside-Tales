from django.contrib import admin
from .models import Contact


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


admin.site.register(Contact, ContactAdmin)