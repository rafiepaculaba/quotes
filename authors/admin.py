from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'author_name', 'born', 'died', 'work', 'pic','bio', 'status')


admin.site.register(Author, AuthorAdmin)
