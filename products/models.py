from django.db import models
from django.db.models import Q

from User.models import User


class Category(models.Model):
    objects = models.Manager()
    categoryID = models.IntegerField(primary_key=True)
    categoryName = models.TextField(max_length=20)

    def __str__(self):
        return self.categoryName  # abidoooooooooooooooo

    def addCategory(self, categoryID, categoryName):
        self.categoryID = categoryID
        self.categoryName = categoryName
        Category.save()

    def deleteCategory(self, categoryID):
        Category.objects.get(self.categoryID == categoryID).delete()

    def modifyCategoryName(self, newName):
        self.categoryName = newName
        Category.save()

    def getAllCategories(self):
        categories = Category.objects.all()
        return categories

class SubCategory(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCatName = models.CharField(max_length=100)

    def __str__(self):
        return self.subCatName

    def getSubcategoryByCategoryID(self, currentCategoryID):
        allSubcategories=SubCategory.objects.all()
        filteredSubCategories=[]
        for subcategory in allSubcategories:
            if subcategory.category.categoryID == int(currentCategoryID):
                filteredSubCategories.append(subcategory.subCatName)

        return filteredSubCategories

class Products(models.Model):
    objects = models.Manager()
    productID = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=200)
    productDetails = models.CharField(max_length=500)
    productImg = models.ImageField(blank=True, null=True)
    categoryID = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    productModel = models.CharField(max_length=200)
    productAverageRating = models.IntegerField(default=0)
    productCount = models.IntegerField(default=0)
    productPrice = models.IntegerField(default=0)


    def deceaseCount(self, current_id):
        product = Products.objects.get(id=current_id)
        product.productCount -= 1
        product.save()

    def getProductsByCategory(self, category_ID):
        products = Products.objects.all()
        matchedProducts = []
        for product in products:
            print(product.categoryID.categoryID)
            if product.categoryID.categoryID == category_ID:
                matchedProducts.append(product)
        return matchedProducts

    def getAllProducts(self):
        products = Products.objects.all()
        return products

    def __str__(self):
        return self.productName



class Reviews(models.Model):
    objects = models.Manager()
    productID = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)

    @classmethod
    def addReview(cls, new_review):
        review = Reviews()
        review.userID = new_review.userID
        review.productID = new_review.productID
        review.review = new_review.review
        review.save()

    @classmethod
    def removeReview(cls, userID, productID):
        Reviews.objects.get(Q(userID=userID) & Q(productID=productID))

    def getReviewsByProductID(self, currentProductID):
        allReviews = Reviews.objects.all()
        matchedReviews = []
        for review in allReviews:
            if review.productID.productID == int(currentProductID):
                matchedReviews.append(review.review)

        return matchedReviews

    class Meta:
        unique_together = ('productID', 'userID')
