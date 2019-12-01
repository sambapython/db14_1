"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import fun, view_products1
from app2.views import view_products2
'''
from django.http import HttpResponse
def fun(request):
	return HttpResponse("hello")
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/",fun), #fun(request_object)
    path("products1/",view_products1),
     path("products2/",view_products2),
]
