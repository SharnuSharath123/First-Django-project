from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html", {'name':'Sharath'})

def add(request):

    # for get method
    # val1 = int(request.GET['num1'])
    # val2 = int(request.GET['num2'])
    # res = val1 + val2

    #for post method
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return render(request, "result.html", {'Result': res})