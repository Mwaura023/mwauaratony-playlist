from django.shortcuts import render, get_object_or_404
from .models import Category
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def reset_admin_password(request):
    """Reset admin password to a temporary one - PUBLIC ACCESS"""
    try:
        User = get_user_model()
        
        # Get or create admin user
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@mwauaratony.com', 
                'is_staff': True, 
                'is_superuser': True,
                'is_active': True
            }
        )
        
        # Set temporary password
        temp_password = 'admin123'
        user.set_password(temp_password)
        user.save()
        
        return HttpResponse(
            f"✅ Admin password reset successfully!<br><br>"
            f"<strong>Username:</strong> admin<br>"
            f"<strong>Password:</strong> {temp_password}<br><br>"
            f"<a href='/admin/'>Go to Admin Panel</a>"
        )
    
    except Exception as e:
        return HttpResponse(f"❌ Error: {str(e)}")

def home(request):
    categories = Category.objects.all()
    return render(request, 'playlist/home.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'playlist/category.html', {'category': category})


def health_check(request):
    return HttpResponse("OK", status=200)
