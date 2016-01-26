from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says : Hello World! <br/> <a href='/Rango/about'>About</a>")
	
def about(request):
	return HttpResponse("Rango says that this is the about page! <br/> <a href='/Rango'>Back!</a>")
