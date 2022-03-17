from django.shortcuts import render
from store.models import Product, Order
from django.db.models.aggregates import Count, Max, Min, Sum, Avg


def say_hello(request):
    result = Product.objects.filter(collection__id=3).aggregate(count=Count('id'), min_price=Min('unit_price'))

    return render(request, 'hello.html', {'name': 'Youssef', 'result': result})
