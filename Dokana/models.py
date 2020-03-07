from django.db import models

# Create your models here.
class Category(models.Model):
    categoryID = models.IntegerField(primary_key=True, max_length=10)
    categoryName = models.TextField(max_length=20)

    def __str__(self):
        return self.categoryID

    def addCategory(self, categoryID, categoryName):
        self.categoryID = categoryID
        self.categoryName = categoryName
        Category.save()

    def deleteCategory(self, categoryID):
        Category.objects.get(self.categoryID == categoryID).delete()

    def modifyCategoryName(self, newName):
        self.categoryName = newName
        Category.save()