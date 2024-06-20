from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me':"Now i am coming from Firstapp index.html!!!"}
    return render(request, 'Firstapp/index.html', context=my_dict)
