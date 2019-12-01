from django.shortcuts import render

# Create your views here.
def view_products2(request):
	return render(request,"app2/products.html")
