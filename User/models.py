from django.db import models
from django.db.models import Q
from django import forms


class USER(models.Model):
    userId = models.IntegerField(primary_key=True, auto_created=True)
    userName = models.CharField(max_length=30)
    email = models.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    phone = models.IntegerField()
    userImage = models.ImageField(upload_to='user/')

    # insert data to user just ex

    def insertUserData(self):
        insertedUser = USER(userName="hema", email="sfsfs@ada.com", password=123, phone=1313, userImage="")
        insertedUser.save()
        print(insertedUser)

    # myuser=USER()
    # myuser.user_name='ibra'
    # myuser.email='ibra@ahoo.com'
    # myuser.password=123
    # myuser.phone='01022896058'
    # myuser.user_image=''
    # insert_userData(myuser)
    # Saving changes to objects (updates) here function will receive user
    # request as a para

    def updateUser(self,_id):
        # myuser.user_id=1
        # update_user(myuser)
        _updUser = USER.objects.get(userId=_id)
        _updUser.userName = 'ahmed'
        _updUser.email = 'ada@dad'
        _updUser.password = '123'
        _updUser.phone = '314969'
        _updUser.userImage = ''
        _updUser.save()

    # get all users >>>> The all() method returns a QuerySet of all the objects in the database.
    def selectAllUsers(self):
        allUsers = USER.objects.all()
        print(allUsers)
        return allUsers

    # Retrieving a single user with get() method
    def selectUserById(self,_id):
        selectUser = USER.objects.get(userId=_id)
        print(selectUser)
        return selectUser

    # delete user by id
    def deleteUser(self,_id):
        USER.objects.filter(userId=_id).delete()


class Address(models.Model):
    userID = models.ForeignKey(to=USER, on_delete=models.CASCADE)
    address = models.TextField(max_length=500)

    def __str__(self):
        return "UserId : " + self.userID + "Address :" + self.address

    def addAddress(self, address):
        add = Address()
        add.userID = address.userID
        add.address = address.address
        add.save()

    def deleteAddress(self, userID, address):
        Address.objects.get(Q(userID=userID) & Q(address=address)).delete()

    class Meta:
        unique_together = ('userID', 'address')
