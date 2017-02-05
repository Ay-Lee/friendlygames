from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import IFriendlyForm
import os
import sys
import datetime
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
			prov5 = "wvlaanderen"
			prov6 = "nationaal"
			dag,mnd,yr = datum.split("/")
			wd = datetime.datetime.strptime(datum, "%d/%m/%Y").weekday()
			responseant = myfunctions.searchteam(leeftijd, prov1, datum)
			responselim = myfunctions.searchteam(leeftijd, prov2, datum)
			responsebra = myfunctions.searchteam(leeftijd, prov3, datum)
			responseovl = myfunctions.searchteam(leeftijd, prov4, datum)
			responsewvl = myfunctions.searchteam(leeftijd, prov5, datum)
			responsenat = myfunctions.searchteam(leeftijd, prov6, datum)
			if (wd == 5 or wd==6):
				stext = leeftijd + " ploegen vrij in het weekend van " + datum + ", klik om de ploegen te zien:"
			else:	
				stext = leeftijd + " ploegen vrij op " + datum + ", klik op ""prov"" om de ploegen te zien per provincie:"
			return render_to_response('search.html', {'antwerpen': responseant.items(), 'limburg': responselim.items(), 'brabant': responsebra.items(),'oostvlaanderen': responseovl.items(), 'westvlaanderen': responsewvl.items(), 'nationaal': responsenat.items(), 'datum': datum, 'leeftijd': leeftijd, 'text':stext})	
	else:
		form = IFriendlyForm()
	return render(request, 'index.html', {'form': form})


def about(request):
	return render_to_response('about.html')
def freeteam(request):
	return HttpResponse("nothing here")


	

