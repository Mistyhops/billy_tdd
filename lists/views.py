from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


def home_page(request: WSGIRequest):
    """Домашняя страница"""
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})
