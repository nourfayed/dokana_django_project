from django.db import models


class Product(models.Model):
    productID = models.IntegerField(primary_key=True)
    productName = models.TextField(default="test")

    def __str__(self):
        return str(self.productID)


class User(models.Model):
    userID = models.IntegerField(primary_key=True)
    userName = models.TextField(default="test")

    def __str__(self):
        return self.userName


class Cart(models.Model):
    productID = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['productID', 'userID']]

    def __str__(self):
        return str(self.productID)

    def removeFromCart(self, productID):
        Cart.objects.get(self.productID == productID).delete()

    def addProductToCart(self, productID, userID):
        self.productID.productID = productID
        self.userID.userID = userID
        self.save()

    def getUserCart(self, userID):
        return Cart.objects.get(self.userID == userID)
