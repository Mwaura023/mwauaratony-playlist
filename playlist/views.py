from django.shortcuts import render, get_object_or_404
from .models import Category
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def reset_admin_password(request):
    """Reset admin password to a temporary one"""
    try:
        User = get_user_model()
        
        # Get or create admin user
        user, created = User.objects.get_or_create(
            username='tony',
            defaults={'email': 'admin@mwauaratony.com', 'is_staff': True, 'is_superuser': True}
        )
        
        # Set temporary password
        temp_password = 'Cnd8301q25'  # Change this after login!
        user.set_password(temp_password)
        user.save()
        
        return HttpResponse(f"Admin password reset! Username: admin, Password: {temp_password}")
    
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def home(request):
    categories = Category.objects.all()
    return render(request, 'playlist/home.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'playlist/category.html', {'category': category})
