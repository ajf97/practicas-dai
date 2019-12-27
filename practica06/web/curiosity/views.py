from django.shortcuts import render, HttpResponse, render_to_response
from django.shortcuts import redirect, get_object_or_404
from django.template import RequestContext
from .forms import MusicianForm, AlbumForm, MusicalGroupForm, UserForm
from .models import Musician, Album, MusicalGroup
from django.contrib.auth.decorators import login_required

import logging 

log = logging.getLogger(__name__) # Para mostrar mensajes por consola con log.error


def index(request):
    return render(request, 'index.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def about(request):
    return render(request, 'about.html', {})


def curiosity(request):
    return render(request, 'curiosity.html', {})


def ephemeris(request):
    return render(request, 'ephemeris.html', {})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        user.password = '' # Lo indicamos para mostrar la contraseña en blanco en el form
        # Lo anterior no cambia la contraseña del usuario
        form = UserForm(instance=user)

    return render(request, 'edit_profile.html', {'form':form})


@login_required
def musician_new(request):
    if request.method == "POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            musician = form.save()
            return redirect('musician_detail', pk=musician.pk)
    else:
        form = MusicianForm()

    return render(request, 'musician_edit.html', {'form':form})


@login_required
def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician_list.html', {'musicians': musicians})


@login_required
def musician_detail(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    return render(request, 'musician_detail.html', {'musician': musician})


@login_required
def musician_edit(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect('musician_detail', pk=musician.pk)
    else:
        form = MusicianForm(instance=musician)

    return render(request, 'musician_edit.html', {'form':form})


@login_required
def musician_delete(request, pk):
    musician = get_object_or_404(Musician, pk=pk)
    musician.delete()
    return redirect('musician_list')


@login_required
def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()

    return render(request, 'album_edit.html', {'form':form})


@login_required
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})


@login_required
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})


@login_required
def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)

    return render(request, 'album_edit.html', {'form':form})


@login_required
def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')


@login_required
def musicalgroup_new(request):
    if request.method == "POST":
        form = MusicalGroupForm(request.POST)
        if form.is_valid():
            musicalgroup = form.save()
            return redirect('musicalgroup_detail', pk=musicalgroup.pk)
    else:
        form = MusicalGroupForm()

    return render(request, 'musicalgroup_edit.html', {'form':form})


@login_required
def musicalgroup_list(request):
    musicalgroups = MusicalGroup.objects.all()
    return render(request, 'musicalgroup_list.html', {'musicalgroups': musicalgroups})


@login_required
def musicalgroup_detail(request, pk):
    musicalgroup = get_object_or_404(MusicalGroup, pk=pk)
    return render(request, 'musicalgroup_detail.html', {'musicalgroup': musicalgroup, 'musicians': musicalgroup.musicians.all()})


@login_required
def musicalgroup_edit(request, pk):
    musicalgroup = get_object_or_404(MusicalGroup, pk=pk)
    if request.method == "POST":
        form = MusicalGroupForm(request.POST, instance=musicalgroup)
        if form.is_valid():
            musicalgroup = form.save()
            return redirect('musicalgroup_detail', pk=musicalgroup.pk)
    else:
        form = MusicalGroupForm(instance=musicalgroup)

    return render(request, 'musicalgroup_edit.html', {'form':form})


@login_required
def musicalgroup_delete(request, pk):
    musicalgroup = get_object_or_404(musicalgroup, pk=pk)
    musicalgroup.delete()
    return redirect('musicalgroup_list')


# La página de error 404 personalizada solo se ve cuando DEBUG=False (modo producción)
