from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, Artist, Release

class releases(ListView):
    model = Release
    template_name = 'release_list.html'
