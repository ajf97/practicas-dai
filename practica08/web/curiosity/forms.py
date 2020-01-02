from django import forms

from .models import MusicalGroup, Album, Musician
from django.contrib.auth.models import User

class MusicalGroupForm(forms.ModelForm):
    class Meta:
        model = MusicalGroup
        fields = ('name', 'created_date', 'style', 'musicians', 'albums')


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'record_company', 'release_date')


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ('name', 'birth_date', 'instrument', 'birth_city', 'latitude', 'longitude')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')