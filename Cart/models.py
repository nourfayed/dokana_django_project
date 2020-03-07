from django.db import models

# Create your models here.
class Cart(models.Model):
    PAYMENT_TYPES = (
        ('c', 'cash'),
        ('v', 'visa')
    )
    paymentMethod = models.CharField(choices=PAYMENT_TYPES, max_length=50)
    productID = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['productID', 'userID']]

    def __str__(self):
        return self.productID

    def removeFromCart(self, productID):
        Cart.objects.get(self.productID == productID).delete()

    def addProductToCart(self,paymentMethod , productID , userID):
        self.paymentMethod = paymentMethod
        self.productID = productID
        self.userID = userID

        Cart.save()

    def getUserCart(self, userID):
        return Cart.objects.get(self.userID == userID)