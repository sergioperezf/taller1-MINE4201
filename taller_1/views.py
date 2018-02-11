from django.shortcuts import render
from django.http import HttpResponse
from os.path import exists

def index(request):
	return render(request, 'taller_1/taller_1.html')