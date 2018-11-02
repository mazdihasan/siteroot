from django.contrib import admin

# Register your models here.
from .models import Post

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'post_slug': ['post_title'],
    }


admin.site.register(Post, AuthorAdmin)
"""
admin.site.register(Post)
"""
