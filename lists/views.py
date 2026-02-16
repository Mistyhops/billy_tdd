from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request: WSGIRequest):
    """Домашняя страница"""
    return render(
        request,
        'home.html',
    )


def view_list(request: WSGIRequest):
    """Представление списка"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request: WSGIRequest):
    """Новый список"""
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-one-list/')
