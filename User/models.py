from django.db import models


# Create your models here.
class User(models.Model):
    userID = models.IntegerField(primary_key=True)


class Address(models.Model):
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500)

    def __str__(self):
        return "UserId : " + self.userID + "Address :" + self.address

    def addAddress(self, address):
        add = Address()
        add.userID = address.userID
        add.address = address.address
        add.save()

    def deleteAddress(self,):
        pass

    class Meta:
        unique_together = ('userID', 'address')
