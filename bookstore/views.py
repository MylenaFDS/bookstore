from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world.html')


def order_detail(request, pk):
    return HttpResponse(f"Order detail for order ID: {pk}")


def product_detail(request, pk):
    return HttpResponse(f"Product detail for product ID: {pk}")


def category_list(request):
    return HttpResponse("Category list")


def category_detail(request, pk):
    return HttpResponse(f"Category detail for category ID: {pk}")

