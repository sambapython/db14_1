from django.shortcuts import render,redirect
from product.forms import ProductForm
from product.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def deleteproduct(request,pk):
	msg=""
	product = Product.objects.get(id=pk)
	if request.method=="POST":
		product.delete()
		return redirect("/")
	else:
		form=ProductForm(instance=product)
	return render(request,"product/check_product.html",
		{"form":form,"message":msg})

@login_required
def updateproduct(request,pk):
	msg=""
	product = Product.objects.get(id=pk)
	if request.method=="POST":
		form=ProductForm(instance=product,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
		else:
			msg=form._erorrs
	else:
		form=ProductForm(instance=product)
	return render(request,"product/product_form.html",
		{"form":form,"message":msg})

@login_required
def createproduct(request):
	if request.method=="POST":
		form = ProductForm(request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			msg="product created successfully"
			return redirect("/")
		else:
			msg = form._errors

	else:
		form = ProductForm()
		msg=""
	return render(request, "product/product_form.html",{"form":form,"message":msg})