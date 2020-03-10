from django.db.models import Q
from django.shortcuts import render
from .models import Category, Products


# Create your views here.
def index(request):
    latest_products = Products.objects.get(pk=1)
    print("w eh kaman")
    print(latest_products)
    Data = {'latest_products': latest_products}
    return render(request, 'products/index.html', Data)


def search(request):
    productName = request.POST.get('product', '')
    category = request.POST.get('category', '')
    min_price = request.POST.get('min_price', '')
    max_price = request.POST.get('max_price', '')
    min_rate = request.POST.get('min_rate', '')
    max_rate = request.POST.get('max_rate', '')

    if category == '':
        category = 'All'
    if min_price == '':
        min_price = '0'
    if max_price == '':
        max_price = '100000'
    if min_rate == '':
        min_rate = '1'
    if max_rate == '':
        max_rate = '5'

    search_filter = {
        'name': productName,
        'cat': category,
        'min_p': min_price,
        'max_p': max_price,
        "min_r": min_rate,
        'max_r': max_rate
    }

    categories = Category.objects.all()

    products = Products.objects.filter(Q(productName__contains=productName))
    if products:
        products = filter(lambda x: price__less_than(max_price, x), products)
        products = filter(lambda x: price__more_than(min_price, x), products)
        products = filter(lambda x: rate__less_than(max_rate, x), products)
        products = filter(lambda x: rate__more_than(min_rate, x), products)
        products = list(products)
        print(len(products))

    else:
        print('Nothing')

    return render(request, 'products/search_result.html',
                  {'filter': search_filter, 'cats': categories, products: 'products'})


def price__less_than(max, product):
    return int(product.productPrice) <= int(max)


def price__more_than(min, element):
    return int(element.productPrice) >= int(min)


def rate__less_than(max, product):
    return int(product.productAverage_rating) <= int(max)


def rate__more_than(min, element):
    return int(element.productAverage_rating) >= int(min)
