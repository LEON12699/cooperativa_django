# Generated by Django 2.2.6 on 2019-11-01 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20191024_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='numero',
            field=models.CharField(help_text='Ingrese numero', max_length=20, unique=True),
        ),
    ]