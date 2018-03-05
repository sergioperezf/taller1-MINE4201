from django.shortcuts import render
from django.http import HttpResponse
from os.path import exists
from taller_1.services import get_possible_artists, get_recommendation_by_artists

def index(request):
	if (request.method == 'GET'):
		return render(request, 'taller_1/taller_1.html', {'artists': get_possible_artists()})
	else:
		recommendations = get_recommendation_by_artists(request.POST.getlist('artists'))
		return render(request, 'taller_1/taller_1.html', {'recommendations': recommendations, 'artists': get_possible_artists()})

def notebook(request):
	return render(request, 'taller_1/notebook.html')