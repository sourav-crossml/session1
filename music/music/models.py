from django.db import models

# Create your models here.
class Singer(models.Model):
    singer_name=models.CharField(max_length=200)
    
class Album(models.Model):
    singer_name=models.ManyToManyField(Singer)
    album_name=models.CharField(max_length=200)
    album_lang=models.CharField(max_length=200)
    no_of_songs=models.IntegerField(default=0)
class Song(models.Model):
    album_name=models.ForeignKey(Album,on_delete=models.CASCADE)
    song_name=models.CharField(max_length=200)
    song_length=models.IntegerField(default=0)