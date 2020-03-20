from .forms import ReviewForm
from User.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from .models import Category, Products, SubCategory, Reviews


def index(request):
    products = Products()
    categories = Category()

    latest_products = products.getAllProducts()

    availableCategories = categories.getAllCategories()
    allSubcategories = getSubcategoryForEachCategory(availableCategories)

    data = {'latest_products': latest_products, 'allSubcategories': allSubcategories}
    return render(request, 'products/index.html', data)


def showDetails(request):
    currentProductId = request.POST.get('productID', '')

    product = Products.objects.get(productID=currentProductId)

    formReview = ReviewForm(request.POST)
    if formReview.is_valid():
        review = formReview.save(commit=False)
        review.productID = product

        userid = request.session["id"]
        user = User.objects.get(userId=userid)

        review.userID = user
        review.save()

    categories = Category()
    availableCategories = categories.getAllCategories()

    allSubcategories = getSubcategoryForEachCategory(availableCategories)

    reviews = Reviews()
    pastReviews = reviews.getReviewsByProductID(currentProductId)

    data = {'product': product, 'formReview': formReview, 'allSubcategories': allSubcategories,
            'pastReviews': pastReviews}

    return render(request, "products/productDetails.html", data)


def showByCategory(request, category_sent, type):
    products = Products()
    categories = Category()

    if type == "category":
        availableProducts = products.getProductsByCategory(category_sent)
    else:
        availableProducts = products.getProductsBySubCategory(category_sent)

    availableCategories = categories.getAllCategories()
    allSubcategories = getSubcategoryForEachCategory(availableCategories)

    data = {'latest_products': availableProducts, 'allSubcategories': allSubcategories}

    return render(request, 'products/index.html', data)


def getSubcategoryForEachCategory(availableCategories):
    sub_categories = SubCategory()
    allSubcategories = []
    for category in availableCategories:
        filteredSubcategories = []
        filteredSubcategories.append(category)
        filteredSubcategories += sub_categories.getSubcategoryByCategoryID(category.categoryID)
        allSubcategories.append(filteredSubcategories)
    return allSubcategories


def updateAverageRate(request):
    currentProductID = request.POST.get("productID", '')
    product = Products.objects.get(productID=currentProductID)
    print("ana f updateAverageRate ")
    print(currentProductID)

    categories = Category()
    availableCategories = categories.getAllCategories()
    allSubcategories = getSubcategoryForEachCategory(availableCategories)

    reviews = Reviews()


    formReview = ReviewForm(request.POST)
    if formReview.is_valid():
        review = formReview.save(commit=False)
        review.productID = product
        userid = request.session["id"]
        user = User.objects.get(userId=userid)
        review.userID = user
        review.save()

    pastReviews = reviews.getReviewsByProductID(currentProductID)

    star = request.POST.get("starNumber")
    if star is None: star = 0

    star = int(star)
    if star > 0:
        avgRating = int(product.productAverageRating)
        if avgRating == 0:
            product.productAverageRating = int(star)
        else:
            avgRating += int(star)
            avgRating /= 2
            product.productAverageRating = avgRating

        product.save()

    data = {'product': product, 'formReview': formReview, 'allSubcategories': allSubcategories,
            'pastReviews': pastReviews}
    return render(request, "products/productDetails.html", data)


def search(request):
    productName = request.POST.get('product', '')
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
    if min_price == '':
        min_price = '0'
    if max_price == '':
        max_price = '100000'
    if min_rate == '':
        min_rate = '1'
    if max_rate == '':
        max_rate = '5'

    print(category + " " + min_price + " " + max_price + " " + min_rate + " " + max_price)

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

    if category == 'All':
        products = Products.objects.filter(Q(productName__contains=productName))
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
