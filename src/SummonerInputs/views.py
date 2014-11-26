from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import SummonerInputForm
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.views.generic.edit import FormView
import json
import requests

# Create your views here.
def home(request):
    form = SummonerInputForm (request.POST or None)
    apikey = 'api_key=b574f3e0-1898-4a5f-9454-1cb4d5c5cfb4' 
    host = 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/'
    host1 = 'https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/'
    if form.is_valid():
        gege = form['Summoner']
        r = requests.get(host + str(gege.value()), params={'api_key': 'b574f3e0-1898-4a5f-9454-1cb4d5c5cfb4'})
        data = r.json()
        print data
        #need to normalize summoner names and input
        SummonerID = data[str(gege.value())]["id"]
        zz = requests.get(host1+str(SummonerID)+'/recent', params=apikey)
        stats = zz.json()
        print(stats)
        return stats
        return HttpResponseRedirect('/summonerscore/')
  
    return render_to_response("Front.html",
                              locals(),
                              context_instance= RequestContext(request)
                              )

#def my_render_callback(response):
#class statList(ListView):
    m#odel = stats
    
def summonerscore(request):
    #t = TemplateResponse(request, 'summonerscore.html', zz.json())
    #return t
    return render_to_response("summonerscore.html",
                            locals(),
                             context_instance= RequestContext(request)
                            )