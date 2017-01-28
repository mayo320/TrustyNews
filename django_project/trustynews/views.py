from django.shortcuts import render
from django.http import Http404, HttpResponse
from scripts.watson import hi

# Create your views here.
def index(request):
    context = {}
    return render(request,'index.html',context)
