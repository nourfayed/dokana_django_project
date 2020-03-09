from django.db import models

# Create your models here.
class Category(models.Model):
     category_ID=models.IntegerField(primary_key = True)
     
class Products(models.Model):
    objects=models.Manager()
    product_ID=models.IntegerField(primary_key = True)
    product_name=models.CharField(max_length=200)
    product_details=models.CharField(max_length=500)
    product_img = models.ImageField(blank=True ,null =True) #l soooraaa  yaaaaa
    category_ID= models.ForeignKey(Category, on_delete=models.CASCADE)
    product_model=models.CharField(max_length=200)
    product_average_rating=models.IntegerField(default= 0)
    product_count=models.IntegerField(default=0)

#     def __checkCount__(self):
#         if self.product_count < 0:
#             self.product_count=0
#             # shoof ba2a hanshilo ezai mn l page masalan 

#     def getProductByCategory(self,category_ID):
#         if category_ID== self.category_ID:
#             return self
    
#     def getAllProducts:
#         #nshoof 7owar l select daa
#         pass
#     def deleteProduct(self,productID):
#         if self.product_details==productID:
#             #shoof ba2a han-delete ezai
#             pass



