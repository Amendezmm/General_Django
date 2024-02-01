from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import dbportfolio
# Create your views here.


def portfolio(request):
    listaportfolio = dbportfolio.objects.values()
    template = loader.get_template("portfolio.html")
    context ={
        "listaportfolio" : listaportfolio
    }

    return HttpResponse(template.render(context, request))




