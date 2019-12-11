from django.shortcuts import render, redirect
from product.models import Category
from django.core.cache import cache
import logging
from django.contrib.auth.decorators import login_required 

logger = logging.getLogger(__name__)
@login_required
def getcategory(request,pk):
	key = "category_%s"%pk
	cat = cache.get(key)
	if not cat:
		cat = Category.objects.get(id=pk)
		cache.set(key,cat)
	return render(request, "product/getcategory.html",{"category":cat})
@login_required
def deletecategory(request,pk):
	cat = Category.objects.get(id=pk)
	if request.method == "POST":
		cat.delete()
		cache.delete("category_%s"%pk)
		return redirect("/")
	return render(request, "product/deletecategory.html",{"category":cat})
@login_required
def createcategory(request):
	#data = request.GET
	logger.info("category creating")
	categories =  Category.objects.all()
	logger.info("got all categories")
	if request.method == "POST":
		data=request.POST
		logger.debug("data to create category: %s"%data.get("name"))
		cat = Category(name=data.get("cat_name"))
		cat.save()
		logger.info("category created successfully")
		return redirect("/")
	return render(request, "product/createcategory.html",
		{"categories":categories})
@login_required
def updatecategory(request,pk):
	cat = Category.objects.get(id=pk)
	if request.method == "POST":
		data = request.POST
		cat.name=data.get('cat_name')
		cat.save()
		cache.delete("category_%s"%pk)
		return redirect("/")
	return render(request,"product/updatecategory.html",{"category":cat})

