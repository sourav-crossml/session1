# Generated by Django 3.2.6 on 2021-08-12 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200)),
                ('song_length', models.IntegerField(default=0)),
                ('singer_name', models.ManyToManyField(to='music.Singer')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=200)),
                ('album_lang', models.CharField(max_length=200)),
                ('no_of_songs', models.IntegerField(default=0)),
                ('song_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song')),
            ],
        ),
    ]
