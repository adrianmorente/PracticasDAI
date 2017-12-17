# restaurantes/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import restaurantes
from bson.json_util import dumps

def index(request):
    return render(request, 'restaurantes/index.html', {})

def register(request):
    return render(request, 'restaurantes/register.html', {})

def restaurants(request):
    return render(request, 'restaurantes/restaurants.html', {})

def contact(request):
    return render(request, 'restaurantes/contact.html', {})

def search(request):
    data_field = request.POST.get('field_name')
    field_content = request.POST.get('parameter')
    query = restaurantes.find({ data_field : field_content }).limit(10)
    context = {
        "list" : list(query),
        "data_field" : data_field,
        "field_content" : field_content
    }
    return render(request, 'restaurantes/restaurants.html', context)

def search_ajax(request):
    data_field = request.GET.get('data_field', '')
    print("field: %s" % data_field)
    field_content = request.GET.get('field_content', '')
    print("content: %s" % field_content)
    page_py = int(request.GET.get('page_py', 1))
    query = restaurantes.find({ data_field : field_content }).skip(page_py*10).limit(10)
    return HttpResponse(dumps(query))
