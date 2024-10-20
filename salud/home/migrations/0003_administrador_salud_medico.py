# Generated by Django 5.1.2 on 2024-10-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_tipo_examen'),
    ]

    operations = [
        migrations.CreateModel(
            name='administrador_salud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.TextField()),
                ('ciudad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=12)),
            ],
        ),
    ]
