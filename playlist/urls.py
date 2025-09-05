from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('admin/reset-password//', views.reset_admin_password, name='reset_password'),
    path('health/', views.health_check, name='health_check'),
    path('events/', views.event_finder, name='event_finder'),
    path('events/add/', views.add_event, name='add_event'),
]
