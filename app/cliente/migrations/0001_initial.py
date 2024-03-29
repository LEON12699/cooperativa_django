# Generated by Django 2.2.5 on 2019-10-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('f', 'Femenino'), ('m', 'Masculino')], default='Femenino', max_length=15)),
                ('estadoCivil', models.CharField(choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('viudo', 'Viudo')], default='Soltero', max_length=15)),
                ('correo', models.EmailField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=13)),
                ('celular', models.CharField(max_length=13)),
                ('direccion', models.TextField(default='sin direccion', max_length=50)),
            ],
        ),
    ]
