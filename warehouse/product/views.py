from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category, Product,Transaction

# Create your views here.
def homeview(request):
	#return HttpResponse("Hello")
	products = Product.objects.all()
	categories = Category.objects.all()
	transactions = Transaction.objects.all()
	return render(request,"product/home.html",
		{"categories":categories,"products":products,
		"transactions":transactions})
