from django.db import models
from User.models import User


# Create your models here.
class Product(models.Model):
    productID = models.IntegerField(primary_key=True)


class Reviews(models.Model):
    productID = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)

    class Meta:
        unique_together = ('productID', 'userID')
