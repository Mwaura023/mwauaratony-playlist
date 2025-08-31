import json
import os
import sys
import django
from django.core.serializers.json import DjangoJSONEncoder

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from playlist.models import Category, Playlist

def backup_data():
    print("Starting backup process...")
    
    # Backup Categories
    print("Backing up categories...")
    categories = list(Category.objects.all().values())
    with open('categories.json', 'w', encoding='utf-8') as f:
        json.dump(categories, f, ensure_ascii=False, indent=2, cls=DjangoJSONEncoder)
    
    # Backup Playlists
    print("Backing up playlists...")
    playlists = list(Playlist.objects.all().values())
    with open('playlists.json', 'w', encoding='utf-8') as f:
        json.dump(playlists, f, ensure_ascii=False, indent=2, cls=DjangoJSONEncoder)
    
    # Create a combined backup
    print("Creating combined backup...")
    combined_data = {
        'categories': categories,
        'playlists': playlists
    }
    with open('backup.json', 'w', encoding='utf-8') as f:
        json.dump(combined_data, f, ensure_ascii=False, indent=2, cls=DjangoJSONEncoder)
    
    print("Backup completed successfully!")
    print("Files created: categories.json, playlists.json, backup.json")

if __name__ == '__main__':
    backup_data()