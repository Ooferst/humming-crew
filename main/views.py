from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductsForm
from main.models import Products
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_json_by_id(request, news_id):
    try:
       products_list = Products.objects.get(pk=news_id)
       json_data = serializers.serialize("json", [products_list])
       return HttpResponse(json_data, content_type="application/json")
    except Products.DoesNotExist:
       return HttpResponse(status=404)

def show_json(request):
    products_list = Products.objects.all()
    json_data = serializers.serialize("json", products_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml(request):
    products_list = Products.objects.all()
    xml_data = serializers.serialize("xml", products_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_xml_by_id(request, news_id):
    try:
       products_list = Products.objects.filter(pk=news_id)
       xml_data = serializers.serialize("xml", products_list)
       return HttpResponse(xml_data, content_type="application/xml")
    except Products.DoesNotExist:
       return HttpResponse(status=404)

def show_main(request):
    products_list = Products.objects.all()
    context = {
        'app_name' : 'Humming Crew',
        'npm' : '2406432406',
        'name': 'Hafiz Nathan Vesaputra',
        'class': 'PBP F',
        'products_list': products_list,
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

def show_products(request, id):
    products = get_object_or_404(Products, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)