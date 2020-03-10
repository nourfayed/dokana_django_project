from django.db import models

# Create your models here.
from django.db.models import Q

from User.models import User


class Category(models.Model):
    categoryID = models.IntegerField(primary_key=True)
    categoryName = models.TextField(max_length=20)

    def __str__(self):
        return self.categoryName

    def addCategory(self, categoryID, categoryName):
        self.categoryID = categoryID
        self.categoryName = categoryName
        Category.save()

    def deleteCategory(self, categoryID):
        Category.objects.get(self.categoryID == categoryID).delete()

    def modifyCategoryName(self, newName):
        self.categoryName = newName
        Category.save()


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCatName = models.CharField(max_length=100)

    def __str__(self):
        return self.subCatName

class Products(models.Model):
    objects = models.Manager()
    productID = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=200)
    productDetails = models.CharField(max_length=500)
    productImg = models.ImageField(blank=True, null=True)  # l soooraaa  yaaaaa
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    productModel = models.CharField(max_length=200)
    productAverage_rating = models.IntegerField(default=0)
    productCount = models.IntegerField(default=0)
    productPrice = models.IntegerField(default=0)

    def __str__(self):
        return self.productName


#     def __checkCount__(self):
#         if self.product_count < 0:
#             self.product_count=0
#             # shoof ba2a hanshilo ezai mn l page masalan 

#     def getProductByCategory(self,category_ID):
#         if category_ID== self.category_ID:
#             return self

#     def getAllProducts:
#         #nshoof 7owar l select daa
#         pass
#     def deleteProduct(self,productID):
#         if self.product_details==productID:
#             #shoof ba2a han-delete ezai
#             pass


class Reviews(models.Model):
    productID = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)

    def __str__(self):
        return self.productID.product_name

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

    class Meta:
        unique_together = ('productID', 'userID')
