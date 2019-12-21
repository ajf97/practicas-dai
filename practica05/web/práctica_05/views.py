from django.shortcuts import render, HttpResponse, render_to_response
from django.template import RequestContext

import logging 

log = logging.getLogger(__name__) # Para mostrar mensajes por consola con log.error

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def logout(request):
    pass


def login(request):
    pass


def profile(request):
    pass


def about(request):
    return render(request, 'about.html', {})


def curiosity(request):
    return render(request, 'curiosity.html', {})


def ephemeris(request):
    return render(request, 'ephemeris.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def update_profile(request):
    pass


# La página de error 404 personalizada solo se ve cuando DEBUG=False (modo producción)
