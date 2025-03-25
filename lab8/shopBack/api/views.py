# from itertools import product
# from django.shortcuts import render
from itertools import product

from django.http import JsonResponse, HttpRequest
from api.models import Product
from api.models import Category
from unicodedata import category


# Create your views here.
def get_products(request: HttpRequest) -> JsonResponse:
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

def get_products_by_id(request, id):
    product = Product.objects.get(id=id)
    return JsonResponse(product.to_json(), safe=False)

def get_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)

def get_category_by_id(request, id):
    category = Category.objects.get(id=id)
    return JsonResponse(category.to_json(), safe=False)

def get_products_of_category_by_id(request, id):
    category = Category.objects.get(id=id)
    products = category.products.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)