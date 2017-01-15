from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import IFriendlyForm
import os
import sys
import myfunctions
# Create your views here.

def index(request):
	if request.method == 'POST':
		form = IFriendlyForm(request.POST)
		if form.is_valid():
			leeftijd = form.cleaned_data['leeftijd']
			datum = form.cleaned_data['datum']
			prov1 = "antwerpen"
			prov2 = "limburg"
			prov3 = "brabant"
			prov4 = "ovlaanderen"
			responseant = myfunctions.searchteam(leeftijd, prov1, datum)
			responselim = myfunctions.searchteam(leeftijd, prov2, datum)
			responsebra = myfunctions.searchteam(leeftijd, prov3, datum)
			responseovl = myfunctions.searchteam(leeftijd, prov4, datum)
			return render_to_response('search.html', {'antwerpen': responseant.items(), 'limburg': responselim.items(), 'brabant': responsebra.items(),'oostvlaanderen': responseovl.items(), 'datum': datum, 'leeftijd': leeftijd})
	else:
		form = IFriendlyForm()
	return render(request, 'index.html', {'form': form})


def freeteam(request):
	return HttpResponse("nothing here")


	

