from django.db import models
from django.db.models import Q

from User.models import User


# Create your models here.
class Product(models.Model):
    productID = models.IntegerField(primary_key=True)


class Reviews(models.Model):
    productID = models.ForeignKey(to=Product, on_delete=models.CASCADE)
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

    class Meta:
        unique_together = ('productID', 'userID')


class Category(models.Model):
    categoryID = models.IntegerField(primary_key=True, max_length=10)
    categoryName = models.TextField(max_length=20)

    def __str__(self):
        return self.categoryID

    def addCategory(self, categoryID, categoryName):
        self.categoryID = categoryID
        self.categoryName = categoryName
        Category.save()

    def deleteCategory(self, categoryID):
        Category.objects.get(self.categoryID == categoryID).delete()

    def modifyCategoryName(self, newName):
        self.categoryName = newName
        Category.save()
