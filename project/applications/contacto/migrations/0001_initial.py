# Generated by Django 4.2.6 on 2023-10-18 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('telefono', models.CharField(max_length=90)),
                ('mensaje', models.CharField(max_length=2000)),
            ],
        ),
    ]
