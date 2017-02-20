from django.shortcuts import render

from .models import Topic


def index(request):
    """Home page for Learning Log"""
    return render(request, 'learning_logs/index.html')
