from django.db import models

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=250)

	def __str__(self):
		return self.name

class Product(models.Model):
	name= models.CharField(max_length=250)
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	description = models.TextField(max_length=600)
	pic = models.ImageField(blank=True,null=True)

	def __str__(self):
		return "%s-->%s"%(self.name,self.category)
class Transaction(models.Model):
	types = [("in","STOCK IN"),("out","STOCK OUT")]
	product = models.ForeignKey(Product,on_delete=models.PROTECT)
	quantity = models.IntegerField(default=1)
	type= models.CharField(choices=types,max_length=3)
	description = models.TextField(max_length=600)

