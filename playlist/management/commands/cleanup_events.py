from django.core.management.base import BaseCommand
from django.utils import timezone
from playlist.models import Event

class Command(BaseCommand):
    help = 'Deactivates events that have passed their date'

    def handle(self, *args, **kwargs):
        events = Event.objects.filter(is_active=True, date__lt=timezone.now())
        for event in events:
            event.is_active = False
            event.save()
        self.stdout.write(self.style.SUCCESS(f'Deactivated {events.count()} past events'))