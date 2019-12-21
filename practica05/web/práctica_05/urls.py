from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^logout', views.logout, name='logout'),
  url(r'^login', views.login, name='login'),
  url(r'^profile', views.profile, name='profile'),
  url(r'^update_profile', views.update_profile, name='update_profile'),
  url(r'^about', views.about, name='about'),
  url(r'^curiosity', views.curiosity, name='curiosity'),
  url(r'^ephemeris', views.ephemeris, name='ephemeris'),
  url(r'^signup', views.signup, name='signup'),
]

