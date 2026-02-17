from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item, List


def home_page(request: WSGIRequest):
    """Домашняя страница"""
    return render(
        request,
        'home.html',
    )


def view_list(request: WSGIRequest, list_id: int):
    """Представление списка"""
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def new_list(request: WSGIRequest):
    """Новый список"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request: WSGIRequest, list_id: int):
    """Добавить элемент в список"""
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=list_)
    return redirect(f"/lists/{list_.id}/")
