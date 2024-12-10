# Generated by Django 5.1.3 on 2024-12-04 20:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=500)),
                ('tipo_respuesta', models.CharField(choices=[('texto', 'Texto'), ('opciones', 'Opciones')], max_length=50)),
                ('opciones', models.TextField(blank=True, null=True)),
                ('formulario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='form.formulario')),
            ],
        ),
    ]