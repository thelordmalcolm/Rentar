from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.forms import ModelForm
from rentar.forms import ApartmentForm, LandlordForm, LandlordRatingForm, ApartmentRatingForm
# from django.contrib.auth import authenticate, login
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login as auth_login,
	logout,

)
from django.views.generic import View
from rentar.forms import UserLoginForm, UserRegisterForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def addressview(request):
	return render(request, 'addressview.html')

def contact(request):
	return render(request, 'contact.html')

def rating(request):
	return render(request,'rating.html')

def registration_form(request):
	return render(request,'registration_form.html')

def add_apartment(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = ApartmentForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return add_apartment_rating(request)
		else:
			print (form.errors)
	else:
		form = ApartmentForm()

	return render(request,'add_apartment.html', {'form':form})

def add_landlord(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = LandlordForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print (form.errors)
	else:
		form = LandlordForm()

	return render(request,'add_landlord.html', {'form':form})

def add_apartment_rating(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = ApartmentRatingForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print (form.errors)
	else:
		form = ApartmentRatingForm()

	return render(request,'add_apartment_rating.html', {'form':form}) #change name of html after merging maybe

def add_landlord_rating(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = LandlordRatingForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return add_apartment(request)
		else:
			print (form.errors)
	else:
		form = LandlordRatingForm()

	return render(request,'add_landlord_rating.html', {'form':form}) #change name of html after merging maybe

def login_view(request):
	title = "Login"
	oppTitle = "Create Account"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		auth_login(request,user)

	return render(request, "login_form.html", {"form":form, "title": title, "oppTitle": oppTitle})

def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username=user.username, password=password)		
		auth_login(request,user)
		return redirect("/") # redirects to homepage after registration 

	context = {
		"form": form,
		"title": title
	}
	return render(request, "registration_form.html", context)

def logout_view(request):
	logout(request)
	return render(request, "registration_form.html", {})