# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/music/')
    favorited_by = models.ManyToManyField(User, related_name='favorite_tracks', blank=True)

    def __str__(self):
        return self.title

class Folder(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    music_tracks = models.ManyToManyField(Music, blank=True)

    def __str__(self):
        return self.name

def create_favorites_folder(sender, instance, created, **kwargs):
    if created:
        Folder.objects.create(name='Favorites', owner=instance)

models.signals.post_save.connect(create_favorites_folder, sender=User)
