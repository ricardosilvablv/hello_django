from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome):
    return HttpResponse(f'<h1>Seja bem vindo {nome}!!!</h1>')
