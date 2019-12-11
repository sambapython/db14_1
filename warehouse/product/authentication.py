from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
import requests
from django.http import HttpResponse
def googleauth_view(request, *args, **kwargs):
	code=request.GET.get('code')
    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = "http://localhost:8000/oauth2redirect/"
    resp = requests.post(access_token_uri, json={
        'code':code,
        'redirect_uri':redirect_uri,
        'client_id':settings.CLIENT_ID,
        'client_secret':settings.SECRET_KEY,
        'grant_type':'authorization_code'
    })
    token_data = resp.json().get("access_token")
    resp = requests.get(f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={token_data}")
    user_data = resp.json()
    username = user_data.get("email")
    user = OwnUser.objects.filter(username=username)
    if user:
        user = user[0]
    else:
        user = OwnUser.objects.create_user(username=username,password="1234WERTT")
    login(request, user)
    #this gets the google profile!!
    return redirect("/")
def signingoogle(request):
	token_request_uri = "https://accounts.google.com/o/oauth2/auth"
	response_type = "code"
	client_id = settings.CLIENT_ID
	redirect_uri = "http://localhost:8000/oauth2redirect/"
	scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
	url = f"{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
	resp = requests.get(url)
	return HttpResponse(resp.text)
def signoutview(request):
	logout(request)
	return redirect("/")
def signinview(request):
	msg=""
	if request.method=="POST":
		data = request.POST
		username=data.get("username")
		password=data.get("password")

		user = authenticate(username=username, password=password)
		if user:
			#request.session.update({"user":user})
			login(request,user)
			return redirect("/")
		else:
			msg="issue with authentication details"
	return render(request,"product/signin.html",{"msg":msg})
def signupview(request):
	msg=""
	if request.method=="POST":
		data = request.POST
		form = UserCreationForm(data)
		if form.is_valid():
			user = User(username=data.get("username"),
				password=data.get("password1"))
			user.save()
			user.set_password(data.get("password1"))
			user.save()
			msg="user created succesfully"
		else:
			msg=form._errors
	else:
		form = UserCreationForm()
	return render(request,"product/signup.html",{"form":form,"msg":msg})