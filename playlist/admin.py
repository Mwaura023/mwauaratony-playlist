from django.contrib import admin
from .models import Category, Playlist

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug']
    prepopulated_fields = {'slug': ('title',)}