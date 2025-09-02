from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates an admin user if it doesn\'t exist'

    def handle(self, *args, **options):
        User = get_user_model()
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@mwauaratony.com',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS('✅ Admin user created successfully!\n') +
                'Username: admin\n' +
                'Password: admin123'
            )
        else:
            self.stdout.write(
                self.style.WARNING('⚠️ Admin user already exists')
            )