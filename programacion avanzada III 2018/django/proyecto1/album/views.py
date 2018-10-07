from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category, Photo


def first_view(request):
    return HttpResponse('Esta es mi primera vista!')

def category(request):
    category_list = Category.objects.all()
    category = Category.objects.get(id='1')
    context = {'object_list': category_list,'object': category}
    return render(request, 'album/category.html', context)
