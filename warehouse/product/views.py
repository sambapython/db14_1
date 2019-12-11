from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category, Product,Transaction
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required() # in the request, session dictionary. should have user details.
def homeview(request):
	#return HttpResponse("Hello")
	products = Product.objects.all()
	categories = Category.objects.all()
	transactions = Transaction.objects.all()
	return render(request,"product/home.html",
		{"categories":categories,"products":products,
		"transactions":transactions})
