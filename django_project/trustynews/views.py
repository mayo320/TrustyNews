from django.shortcuts import render
from django.http import Http404, HttpResponse
import json
from scripts.MLAnalysis import *

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html',context)


def searchURL(request):
    if request.method == 'POST':
        _url = request.POST.get('url')

         #calls watson analyze
        response_data = calculate(_url)
        #response_data ={"hi":"hi"}

        return HttpResponse(json.dumps(response_data),content_type='application/json')
    else:
        response_data = {}
        return HttpResponse(json.dumps(response_data),content_type='application/json')
