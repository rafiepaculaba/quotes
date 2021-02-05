from django.http import HttpResponse
from django.shortcuts import render
from .models import Author


def index(request):
    authors = Author.objects.all()
    return render(request, 'index.html', {'authors': authors})


def new(request):
    return HttpResponse('Hello New')


