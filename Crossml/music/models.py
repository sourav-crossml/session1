from django.db import models

# Create your models here.
class Singer(models.Model):
    singer_name=models.CharField(max_length=200)
class Song(models.Model):
    
    song_name=models.CharField(max_length=200)
    song_length=models.IntegerField(default=0)
    singer_name=models.ManyToManyField(Singer)   
class Album(models.Model):
    song_name=models.ForeignKey(Song,on_delete=models.CASCADE)
    album_name=models.CharField(max_length=200)
    album_lang=models.CharField(max_length=200)
    no_of_songs=models.IntegerField(default=0)
