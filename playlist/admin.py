from django.contrib import admin
from .models import Category, Playlist, Event, TicketOption


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}


class TicketOptionInline(admin.TabularInline):
    model = TicketOption
    extra = 1  # always show one empty row for adding new tickets


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'date', 'venue', 'min_ticket_price', 'is_active']
    list_filter = ['genre', 'date', 'is_active']
    search_fields = ['name', 'venue']
    fields = ['name', 'genre', 'date', 'venue', 'description', 'ticket_link', 'image_url', 'is_active']
    inlines = [TicketOptionInline]

    def min_ticket_price(self, obj):
        return obj.min_ticket_price()
    min_ticket_price.short_description = "Lowest Price"
