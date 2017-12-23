# -*- coding: utf-8 -*-
# restaurantes/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import restaurantes
from bson.json_util import dumps
from .forms import RestauranteForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'restaurantes/index.html', {})

def register(request):
    return render(request, 'restaurantes/register.html', {})

def restaurants(request):
    form = RestauranteForm()
    if request.method == 'POST':
        form = RestauranteForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            return redirect('/restaurants')
    return render(request, 'restaurantes/restaurants.html', { 'form' : form })

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
    field_content = request.GET.get('field_content', '')
    page_py = int(request.GET.get('page_py', 1))
    query = restaurantes.find({ data_field : field_content }).skip(page_py*10).limit(10)
    return HttpResponse(dumps(query))

def add_restaurant(request):
    form = RestauranteForm()
    if request.method == 'POST':
        form = RestauranteForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            restaurantes.insert({
             	"address" : {
             		"building" : datos['building'],
             		"street" : datos['street'],
             		"zipcode" : datos['zipcode']
             	},
             	"borough" : datos['borough'],
             	"cuisine" : datos['cuisine'],
            	"name" : datos['name'],
            })
            return redirect('/restaurants')
    return render(request, 'restaurantes/restaurants.html', { 'form' : form })

def charts(request):
    bakery_Bronx = restaurantes.find( { "cuisine": "Bakery", "borough": "Bronx" } ).count()
    american_Bronx = restaurantes.find( { "cuisine": "American", "borough": "Bronx" } ).count()
    hamburgers_Bronx = restaurantes.find( { "cuisine": "Hamburgers", "borough": "Bronx" } ).count()
    pizza_Bronx = restaurantes.find( { "cuisine": "Pizza", "borough": "Bronx" } ).count()

    bakery_Queens = restaurantes.find( { "cuisine": "Bakery", "borough": "Queens" } ).count()
    american_Queens = restaurantes.find( { "cuisine": "American", "borough": "Queens" } ).count()
    hamburgers_Queens = restaurantes.find( { "cuisine": "Hamburgers", "borough": "Queens" } ).count()
    pizza_Queens = restaurantes.find( { "cuisine": "Pizza", "borough": "Queens" } ).count()

    bakery_Brooklyn = restaurantes.find( { "cuisine": "Bakery", "borough": "Brooklyn" } ).count()
    american_Brooklyn = restaurantes.find( { "cuisine": "American", "borough": "Brooklyn" } ).count()
    hamburgers_Brooklyn = restaurantes.find( { "cuisine": "Hamburgers", "borough": "Brooklyn" } ).count()
    pizza_Brooklyn = restaurantes.find( { "cuisine": "Pizza", "borough": "Brooklyn" } ).count()

    bakery_StatenIsland = restaurantes.find( { "cuisine": "Bakery", "borough": "Staten Island" } ).count()
    american_StatenIsland = restaurantes.find( { "cuisine": "American", "borough": "Staten Island" } ).count()
    hamburgers_StatenIsland = restaurantes.find( { "cuisine": "Hamburgers", "borough": "Staten Island" } ).count()
    pizza_StatenIsland = restaurantes.find( { "cuisine": "Pizza", "borough": "Staten Island" } ).count()

    bakery_Manhattan = restaurantes.find( { "cuisine": "Bakery", "borough": "Manhattan" } ).count()
    american_Manhattan = restaurantes.find( { "cuisine": "American", "borough": "Manhattan" } ).count()
    hamburgers_Manhattan = restaurantes.find( { "cuisine": "Hamburgers", "borough": "Manhattan" } ).count()
    pizza_Manhattan = restaurantes.find( { "cuisine": "Pizza", "borough": "Manhattan" } ).count()

    context = {
        'title_page' : "Highcharts stats",
        'bakery' : [bakery_Bronx, bakery_Queens, bakery_Brooklyn, bakery_StatenIsland, bakery_Manhattan],
        'american' : [american_Bronx, american_Queens, american_Brooklyn, american_StatenIsland, american_Manhattan],
        'hamburgers' : [hamburgers_Bronx, hamburgers_Queens, hamburgers_Brooklyn, hamburgers_StatenIsland, hamburgers_Manhattan],
        'pizza' : [pizza_Bronx, pizza_Queens, pizza_Brooklyn, pizza_StatenIsland, pizza_Manhattan],
    }

    return render(request, 'restaurantes/highcharts.html', context)
