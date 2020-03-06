from django.db import models


# Create your models here.
class User(models.Model):
    userID = models.IntegerField(primary_key=True)


class Address(models.Model):
    userID = models.ForeignKey(to=User, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self):
        return "UserId : " + self.userID + "Address :" + self.address

    def addAddress(self):
        pass

    class Meta:
        unique_together = ('userID', 'address')
