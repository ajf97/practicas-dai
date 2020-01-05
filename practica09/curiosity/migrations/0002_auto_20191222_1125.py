# Generated by Django 2.2.9 on 2019-12-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curiosity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='musicalgroup',
            name='created_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
