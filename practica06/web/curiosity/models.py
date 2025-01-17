from django.db import models
from django.utils import timezone

class Musician(models.Model):
    name = models.CharField(max_length=35)
    birth_date = models.DateField(blank=False, null=True)
    instrument = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class MusicalGroup(models.Model):
    name = models.CharField(max_length=35)
    created_date = models.DateField(blank=True, null=True)
    style = models.CharField(max_length=20)
    musicians = models.ManyToManyField(Musician)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=20)
    record_company = models.CharField(max_length=25)
    release_date = models.DateField(blank=False, null=True)
    musicalgroup = models.ForeignKey(MusicalGroup,  on_delete=models.CASCADE,
    blank=False, null=True)

    def __str__(self):
        return self.title


