from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def pur_view(request):
	# res="""
	# <h1>HELLO</h1>
	# """
	#return HttpResponse("hello")
	#return HttpResponse(res)
	# I need to read the html data from index.html, create HttpResponse object.
	return render(request,"pur/index.html")
