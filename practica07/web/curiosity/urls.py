from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^profile', views.profile, name='profile'),
  url(r'^edit_profile', views.edit_profile, name='edit_profile'),
  url(r'^about', views.about, name='about'),
  url(r'^curiosity', views.curiosity, name='curiosity'),
  url(r'^ephemeris', views.ephemeris, name='ephemeris'),
  url(r'get_data', views.reclama_datos, name='reclama_datos'),

  path('musician/<int:pk>/', views.musician_detail, name='musician_detail'),
  url(r'^musician/new', views.musician_new, name='musician_new'),
  url(r'^musician/list', views.musician_list, name='musician_list'),
  path('musician/<int:pk>/edit/', views.musician_edit, name='musician_edit'),
  path('musician/<int:pk>/delete/', views.musician_delete, name='musician_delete'),


  path('album/<int:pk>/', views.album_detail, name='album_detail'),
  url(r'^album/new', views.album_new, name='album_new'),
  url(r'^album/list', views.album_list, name='album_list'),
  path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
  path('album/<int:pk>/delete/', views.album_delete, name='album_delete'),


  path('musicalgroup/<int:pk>/', views.musicalgroup_detail, name='musicalgroup_detail'),
  url(r'^musicalgroup/new', views.musicalgroup_new, name='musicalgroup_new'),
  url(r'^musicalgroup/list', views.musicalgroup_list, name='musicalgroup_list'),
  path('musicalgroup/<int:pk>/edit/', views.musicalgroup_edit, name='musicalgroup_edit'),
  path('musicalgroup/<int:pk>/delete/', views.musicalgroup_delete, name='musicalgroup_delete'),
]

