from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model
import os

def create_admin_user(sender, **kwargs):
    # Only create on Render production
    if os.environ.get('RENDER'):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            print('✅ Admin user created automatically: admin / admin123')

class PlaylistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playlist'

    def ready(self):
        post_migrate.connect(create_admin_user, sender=self)