from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'bio', 'status')


admin.site.register(Author, AuthorAdmin)
