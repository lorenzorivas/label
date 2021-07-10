from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

class Category(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Titulo Categoria')
    slug = AutoSlugField(populate_from = 'title', always_update = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Categoria'
        ordering = ['-id']

class Artist(models.Model):
    name = models.CharField(max_length = 255, unique = True, verbose_name = 'Nombre Productor')
    slug = AutoSlugField(populate_from = 'name', always_update = True)
    bio = HTMLField()
    image = models.URLField(max_length = 255, blank = True, null = False)
    facebook_link = models.URLField(max_length = 255, blank = True, null = False)
    twitter_link = models.URLField(max_length = 255, blank = True, null = False)
    instagram_link = models.URLField(max_length = 255, blank = True, null = False)
    youtube_link = models.URLField(max_length = 255, blank = True, null = False)
    web_link = models.URLField(max_length = 255, blank = True, null = False)
    state = models.BooleanField('Activar/Desactivar Productor', default = True)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Productor'
        verbose_name_plural = 'Productores'

class Release(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Titulo Lanzamiento')
    slug = AutoSlugField(populate_from = 'title', always_update = True)
    artist = models.ForeignKey(Artist, on_delete = models.CASCADE, blank = True, null = False, verbose_name = 'Artista')
    category = models.ManyToManyField(Category, verbose_name = 'Categoria')
    image = models.URLField(max_length = 255, blank = True, null = False)
    date_added = models.DateTimeField(auto_now_add = True)
    iframe = models.TextField(null = False)
    published = models.BooleanField('Publicar', default = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lanzamiento'
