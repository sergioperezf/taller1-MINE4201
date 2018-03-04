from django.shortcuts import render
from django.http import HttpResponse
from os.path import exists
from taller_1.services import get_possible_artists

def index(request):
	if (request.method is 'GET'):
		return render(request, 'taller_1/taller_1.html', get_possible_artists())
	else:
		# todo process form
		return render(request, 'taller_1/taller_1.html', get_possible_artists())