from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fun(request):
	return HttpResponse("hello")
def view_products1(request):
	'''
	resp="""
	<html>
	<h1>"NOKIA,","MI,","SAMSUNG"</h1>
	</html>
	"""
	return HttpResponse(resp)
	'''
	# Render will check settings.installed_apps
	return render(request,"app1/products.html")
