# Generated by Django 4.0.4 on 2022-05-02 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateTimeField()),
                ('imagen_miniatura', models.ImageField(default='miniaturacapacitaciondefault.jpg', upload_to='miniaturas_capacitaciones')),
                ('imagen_portada', models.ImageField(default='portadacapacitaciondefault.jpg', upload_to='portadas_capacitaciones')),
                ('link_capacitacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Operaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField(auto_now=True)),
                ('producto', models.ManyToManyField(to='AppTienda.capacitacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('producto', models.ManyToManyField(to='AppTienda.capacitacion')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
