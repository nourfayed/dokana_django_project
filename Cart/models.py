from django.db import models

# Create your models here.
from django.db import models

from Dokana.models import Product
from User.models import User


class History(models.Model):
    PAYMENT_TYPES = (
        ('c', 'cash'),
        ('v', 'visa')
    )

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
