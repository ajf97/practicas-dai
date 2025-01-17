# Generated by Django 2.2.9 on 2020-01-02 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curiosity', '0002_auto_20191222_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='birth_city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='musician',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
