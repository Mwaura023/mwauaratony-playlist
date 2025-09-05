# playlist/models.py
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

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


class Event(models.Model):
    GENRE_CHOICES = [
        ('reggae', 'Reggae/Riddims'),
        ('rhumba', 'Rhumba'),
        ('mugithi', 'Mugithi'),
        ('rnb', 'RnB'),
        ('soul', 'Soul'),
    ]

    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='reggae')
    date = models.DateTimeField()
    venue = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ticket_link = models.URLField(blank=True)
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def is_upcoming(self):
        return self.is_active and self.date >= timezone.now()

    def min_ticket_price(self):
        """Return cheapest ticket price (used for filtering)."""
        prices = [t.numeric_price() for t in self.tickets.all()]
        return min(prices) if prices else 0

    class Meta:
        ordering = ['date']


class TicketOption(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    label = models.CharField(max_length=100)  # e.g. VIP, Regular, Early Bird
    price = models.CharField(max_length=100)

    def numeric_price(self):
        """Extract a number from the price string for filtering."""
        price_str = self.price.lower().strip()
        if "free" in price_str:
            return 0
        price_str = price_str.replace("ksh", "").replace(",", "").strip()
        try:
            return int(''.join(filter(str.isdigit, price_str)))
        except:
            return 0

    def __str__(self):
        return f"{self.label}: {self.price}"