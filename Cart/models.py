from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from User.models import User
from products.models import Products

PAYMENT_TYPES = (
    ('c', 'cash'),
    ('v', 'visa')
)


class History(models.Model):
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    productID = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    paymentMethod = models.CharField(choices=PAYMENT_TYPES, max_length=50)
    date = models.DateTimeField()
    count = models.IntegerField(default=1)

    def __str__(self):
        return 'userId: ' + self.userID.userId.__str__() + 'productId: ' + self.productID.productID.__str__() + 'payment: ' + self.paymentMethod

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

    def deleteUserHistory(self, pk):
        History.objects.get(self.pk == userID).delete()

    class Meta:
        unique_together = ('userID', 'productID','date')


class Cart(models.Model):
    count = models.IntegerField(default=1)
    productID = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.productID)

    def removeFromCart(self, productID):
        Cart.objects.get(self.productID == productID).delete()

    def addProductToCart(self, paymentMethod, productID, userID):
        self.paymentMethod = paymentMethod
        self.productID = productID
        self.userID = userID

        Cart.save()

    def getUserCart(self, userID):
        return Cart.objects.get(self.userID == userID)

    class Meta:
        unique_together = ('productID', 'userID')
# delete user cart functon when the user deactivated
    def deleteUserCart(self,userID):
        Cart.objects.get(self.userID == userID).delete()