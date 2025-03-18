# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post

class CustomUserAdmin(UserAdmin):
    # Add your new fields to both 'fieldsets' (edit view) and 'add_fieldsets' (create view)
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('age', 'bio')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {
            'fields': ('age', 'bio'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)
