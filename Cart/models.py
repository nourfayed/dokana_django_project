from django.db import models

# Create your models here.
from django.db import models

from Dokana.models import Product
from User.models import User

PAYMENT_TYPES = (
    ('c', 'cash'),
    ('v', 'visa')
)


class History(models.Model):
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    productID = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    paymentMethod = models.CharField(choices=PAYMENT_TYPES, max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return 'userId: ' + self.userID + 'productId: ' + self.productID + 'payment: ' + self.paymentMethod

    def getUserHistory(self, userId):
        return History.objects.get(self.userID == userId)

    def addToUserHistory(self, cardList):
        for card in cardList:
            history = History()
            history.userID = card.userID
            history.productID = card.productID
            history.paymentMethod = card.paymentMethod
            history.date = card.date

            history.save()

    def deleteUserHistory(self, userID):
        History.objects.get(self.userID == userID).delete()

    class Meta:
        unique_together = ('userID', 'productID')


class Cart(models.Model):
    paymentMethod = models.CharField(choices=PAYMENT_TYPES, max_length=50)
    productID = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['productID', 'userID']]

    def __str__(self):
        return self.productID

    def removeFromCart(self, productID):
        Cart.objects.get(self.productID == productID).delete()

    def addProductToCart(self, paymentMethod, productID, userID):
        self.paymentMethod = paymentMethod
        self.productID = productID
        self.userID = userID

        Cart.save()

    def getUserCart(self, userID):
        return Cart.objects.get(self.userID == userID)
