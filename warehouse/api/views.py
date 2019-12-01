from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Transaction, Product,\
Category
from rest_framework.serializers import ModelSerializer
from rest_framework import status, viewsets

class CategorySerializer(ModelSerializer):
	class Meta:
		model=Category
		fields = "__all__"

class CategoryView(viewsets.ModelViewSet):
		queryset=Category.objects.all()
		serializer_class = CategorySerializer


class ProductSerializer(ModelSerializer):
	class Meta:
		model = Product 
		fields="__all__"
class ProductPostSerializer(ModelSerializer):
	class Meta:
		model = Product 
		fields="__all__"

class ProductView(APIView):
	def get(self,request):
		data = Product.objects.all()
		ser = ProductSerializer(data,many=True)
		return Response(ser.data)
	def post(self,request):
		resp={"status":"","errors":"","data":""}
		data = request.data
		ser = ProductPostSerializer(data=data)
		if ser.is_valid():
			ser.save()
			resp["status"]="success"
			resp["data"] = ser.data
		else:
			resp["status"]="failed"
			resp["errors"]=ser._errors
		return Response(resp)

class TransactionSerializer(ModelSerializer):
	class Meta:
		model = Transaction 
		fields="__all__"
class TransactionPostSerializer(ModelSerializer):
	class Meta:
		model = Transaction 
		fields="__all__"
class TransactionPutSerializer(ModelSerializer):
	class Meta:
		model = Transaction 
		fields="__all__"
		extra_kwargs = {"product":{"required":False},
		"quantity":{"required":False},
		"type":{"required":False},
		"description":{"required":False}}

# Create your views here.
class TrasactionView(APIView):

	def get(self,request,pk=None):
		resp={"status":"","errors":"","data":""}
		if pk:
			data = Transaction.objects.filter(id=pk)
			if not data:
				resp["status"]="failed"
				resp["errors"]="Not found"
				return Response(resp,status=status.HTTP_404_NOT_FOUND)	
		else:
			data = Transaction.objects.all()
		ser = TransactionSerializer(data,many=True)
		return Response(ser.data)
	def post(self,request):
		resp={"status":"","errors":"","data":""}
		data = request.data
		ser = TransactionPostSerializer(data=data)
		if ser.is_valid():
			ser.save()
			resp["status"]="success"
			resp["data"] = ser.data
		else:
			resp["status"]="failed"
			resp["errors"]=ser._errors
		return Response(resp)
	def put(self,request,pk):
		resp={"status":"","errors":"","data":""}
		tansactions = Transaction.objects.filter(id=pk)
		if tansactions:
			tansaction = tansactions[0]
			ser = TransactionPutSerializer(instance=tansaction,
				data=request.data)
			if ser.is_valid():
				ser.save()
				resp["status"]="success"
				resp["data"] = ser.data
			else:
				resp["status"]="failed"
				resp["errors"]=ser._errors
		else:
			esp["status"]="failed"
			resp["errors"]="transaxction with this is not found"
			return Response(resp,status=status.HTTP_404_NOT_FOUND)
		return Response(resp)
	def delete(self,request,pk):
		resp={"status":"","errors":"","data":""}
		tansactions = Transaction.objects.filter(id=pk)
		if tansactions:
			tansaction = tansactions[0]
			ser = TransactionSerializer(tansactions,many=True)
			tansaction.delete()
			resp["status"]="success"
			resp["data"] = ser.data
		else:
			resp["status"]="failed"
			resp["errors"]="transaction with this id not found"
			return Response(resp,status=status.HTTP_404_NOT_FOUND)
		return Response(resp)
