from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def master(request):
    template = loader.get_template("master.html")
    context = {
        "":"",
    }
    
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template("home.html")
    context = {
        "valor" : "valor"
    }

    return HttpResponse(template.render(context, request))

def contacts(request):
    template = loader.get_template("contacts.html")
    context = {
        "valor" : "valor",
    }
    return HttpResponse(template.render(context,request))

def about(request):
    template = loader.get_template("aboutme.html")
    context ={
        "valor" : "valor",
    }

    return HttpResponse(template.render(context, request)) 


 