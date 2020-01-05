from django.shortcuts import render, HttpResponse, render_to_response
from django.shortcuts import redirect, get_object_or_404
from django.template import RequestContext
from .forms import MusicianForm, AlbumForm, MusicalGroupForm, UserForm
from .models import Musician, Album, MusicalGroup
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator

import logging 

log = logging.getLogger(__name__) # Para mostrar mensajes por consola con log.error

# La página de error 404 personalizada solo se ve cuando DEBUG=False (modo producción)

@login_required
def historial(request, page):
    if 'historial' in request.session:
        encontrado = False
        for elem in request.session['historial']:
            if elem[1] == page[1]:
                encontrado = True
        
        if not encontrado:
            request.session['historial'] = [page] + request.session['historial']

        if len(request.session['historial']) > 3:
            request.session['historial'].pop()
    else:
        request.session['historial'] = [page]



def index(request):
    historial(request, (reverse('index'), 'Inicio'))

    if request.user.is_authenticated:
        context = {'historial': request.session['historial']}
    else:
        context = {}

    return render(request, 'index.html', context)


@login_required
def profile(request):
    historial(request, (reverse('profile'), 'Mi Perfil'))
    context = {'historial': request.session['historial']}
    return render(request, 'profile.html', context)


def about(request):
    historial(request, (reverse('about'), 'Acerca de'))

    if request.user.is_authenticated:
        context = {'historial': request.session['historial']}
    else:
        context = {}

    return render(request, 'about.html', context)


def curiosity(request):
    historial(request, (reverse('curiosity'), 'Curiosidades'))

    if request.user.is_authenticated:
        context = {'historial': request.session['historial']}
    else:
        context = {}

    return render(request, 'curiosity.html', context)


def ephemeris(request):
    historial(request, (reverse('ephemeris'), 'Efemérides'))

    if request.user.is_authenticated:
        context = {'historial': request.session['historial']}
    else:
        context = {}

    return render(request, 'ephemeris.html', context)


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
    historial(request, (reverse('musician_list'), 'Músicos'))
    musicians = Musician.objects.all()
    context = {'musicians': musicians, 'historial': request.session['historial']}
    return render(request, 'musician_list.html', context)


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
    historial(request, (reverse('album_list'), 'Álbum'))
    albums = Album.objects.all()
    context = {'albums': albums, 'historial': request.session['historial']}
    return render(request, 'album_list.html', context)


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
    historial(request, (reverse('musicalgroup_list'), 'Grupos musicales'))
    musicalgroups = MusicalGroup.objects.all()
    context = {'musicalgroups': musicalgroups, 'historial': request.session['historial']}
    return render(request, 'musicalgroup_list.html', context)


@login_required
def musicalgroup_detail(request, pk):
    musicalgroup = get_object_or_404(MusicalGroup, pk=pk)
    context = {'musicalgroup': musicalgroup, 'albums': Album.objects.filter(musicalgroup=pk) ,
                'musicians': musicalgroup.musicians.all()}
    return render(request, 'musicalgroup_detail.html', context)


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
    musicalgroup = get_object_or_404(MusicalGroup, pk=pk)
    musicalgroup.delete()
    return redirect('musicalgroup_list')


@login_required
def reclama_datos(request):
    
    page_size = 3

    musicalgroups = MusicalGroup.objects.all().values()
    paginator = Paginator(musicalgroups, page_size)
    page = request.GET.get('page')
    musicalgroups = paginator.page(page)

    return JsonResponse(list(musicalgroups), safe=False)


@login_required
def maps_charts(request):
    historial(request, (reverse('maps_charts'), 'Mapas y gráficas'))
    count_list = [len(MusicalGroup.objects.all()), len(Musician.objects.all()), len(Album.objects.all())]
    group_names = [ i['name']  for i in MusicalGroup.objects.values('name')[:4]]
    album_counts = [Album.objects.filter(musicalgroup__name=i).count() for i in group_names]
    context = {'historial': request.session['historial'], 'counts': count_list, 'groupnames': group_names, 'albumcounts': album_counts}
    return render(request, 'maps_charts.html', context)