from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem


def say_hello(request):
    queryset = Product.objects.filter(pk__in=OrderItem.objects.values('product__id').distinct()).order_by('title')

    # print(queryset)

    return render(request, 'hello.html', {'name': 'Youssef', 'products': list(queryset)})
