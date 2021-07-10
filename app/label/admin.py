from django.contrib import admin
from .models import Category, Artist, Release

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['category',]

admin.site.register(Category, CategoryAdmin)

class ReleaseAdmin(admin.ModelAdmin):
    autocomplete_fields = ['artist', 'category',]

admin.site.register(Release, ReleaseAdmin)

class ReleaseInline(admin.StackedInline):
    model = Release
    autocomplete_fields = ['artist', 'category',]
    extra = 0

class ArtistAdmin(admin.ModelAdmin):
    inlines = [ReleaseInline]
    search_fields = ['artist',]

admin.site.register(Artist, ArtistAdmin)
