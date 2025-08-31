from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True) 
    image = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="playlists")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    spotify_link = models.URLField(blank=True, null=True)
    drive_link = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
