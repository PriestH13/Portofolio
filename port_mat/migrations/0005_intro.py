# Generated by Django 5.2 on 2025-04-29 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port_mat', '0004_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descrizione', models.TextField()),
                ('immagine', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
