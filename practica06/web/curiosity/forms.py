from django import forms

from .models import MusicalGroup, Album, Musician

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
        fields = ('name', 'birth_date', 'instrument')