from django.shortcuts import render, redirect
from .models import Category, Products
from .forms import ReviewForm
from User.models import User
from django.db.models import Q
from django.shortcuts import render
from .models import Category, Products, SubCategory


# Create your views here.
def index(request):
    products = Products()
    latest_products = products.getAllProducts()
    data = {'latest_products': latest_products}
    return render(request, 'products/index.html', data)

    latest_products = Products.objects.get(pk=1)
    print("w eh kaman")
    print(latest_products)
    Data = {'latest_products': latest_products}
    return render(request, 'products/index.html', Data)


def showDetails(request):
    currentProductId = request.POST.get('productID', '')
    print("Current product id from show details................................")
    print(currentProductId)
    product = Products.objects.get(productID=currentProductId)

    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.productID = product
        user = User()
        user.userId = 1
        user.userName = "7amada"
        user.email = "fgklhkk@gmail.com"
        user.password = "12435465rydf"
        user.phone = 1234546
        user.save()
        review.userID = user
        review.save()
    data = {'product': product, 'form': form}
    return render(request, "products/productDetails.html", data)


def search(request):
    print(request.POST)
    productName = request.POST.get('product', '')
    searchBy = request.POST.get('by', '')
    category = request.POST.get('category', '')
    min_price = request.POST.get('min_price', '')
    max_price = request.POST.get('max_price', '')
    min_rate = request.POST.get('min_rate', '')
    max_rate = request.POST.get('max_rate', '')

    sub_cats = SubCategory.objects.all();
    sub_cats = tuple(sub_cats)
    sub_cats_name = []
    for sub in sub_cats:
        sub_cats_name.append(sub.subCatName)
    sub_cats_name = tuple(sub_cats_name)
    print(sub_cats_name[0])
    print(category)
    if category not in sub_cats_name:
        category = 'All'
    if searchBy == '':
        searchBy = 'product'
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
    cats = tuple(categories)
    if category == "All":
        final_cat = "<option value=" + category + " selected>" + "All" + "</option>"
    else:
        final_cat = "<option value=" + category + ">" + "All" + "</option>"

    for cat in cats:
        final_cat = final_cat + "<optgroup label=" + cat.categoryName + ">"
        subCat = tuple(SubCategory.objects.filter(category=cat))
        for s in subCat:
            if s.subCatName == category:
                final_cat = final_cat + "<option value=" + s.subCatName + " selected>" + s.subCatName + "</option>"
            else:
                final_cat = final_cat + "<option value=" + s.subCatName + ">" + s.subCatName + "</option>"

            # final_cat.append(s.subCatName)
        final_cat = final_cat + "</optgroup>"
        # for s in subCat:
        #     final_cat.append(s.subCatName)
        # # print(subCat)

    if searchBy == 'product':
        products = Products.objects.filter(Q(productName__contains=productName))
    elif searchBy == 'model':
        products = Products.objects.filter(Q(productModel__contains=productName))
    else:
        if category == 'All':
            products = Products.objects.all()
        else:
            cat_id = SubCategory.objects.get(subCatName=category)
            # products = Products.objects.filter(Q(productName__contains=productName) and Q(category=cat_id))
            products = Products.objects.filter(Q(productName__contains=productName) & Q(categoryID=cat_id))

    if products:
        products = filter(lambda x: price__less_than(max_price, x), products)
        products = filter(lambda x: price__more_than(min_price, x), products)
        products = filter(lambda x: rate__less_than(max_rate, x), products)
        products = filter(lambda x: rate__more_than(min_rate, x), products)
        products = tuple(products)
        # products = list(products)
    else:
        print('Nothing')

    return render(request, 'products/search_result.html',
                  {'filter': search_filter, 'cats': final_cat, 'products': products})


def price__less_than(max, product):
    return int(product.productPrice) <= int(max)


def price__more_than(min, element):
    return int(element.productPrice) >= int(min)


def rate__less_than(max, product):
    return int(product.productAverageRating) <= int(max)


def rate__more_than(min, element):
    return int(element.productAverageRating) >= int(min)
