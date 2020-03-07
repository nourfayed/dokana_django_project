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
