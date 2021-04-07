from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

app_name = "app1"

def index(request):
    return render(request,"sample.html")