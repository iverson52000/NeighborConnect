from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request, 'first_app/index.html')

def signin(request):
	return render(request, 'first_app/signin.html')

def register(request):
	return render(request, 'first_app/register.html')

def profile(request):
	return render(request, 'first_app/profile.html')

