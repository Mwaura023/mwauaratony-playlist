# playlist/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Event, TicketOption
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import EventForm
from .forms import EventForm, TicketOptionFormSet


@csrf_exempt
def reset_admin_password(request):
    """Reset admin password to a temporary one - PUBLIC ACCESS"""
    try:
        User = get_user_model()
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@mwauaratony.com',
                'is_staff': True,
                'is_superuser': True,
                'is_active': True
            }
        )
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

def event_finder(request):
    genre = request.GET.get('genre')
    price_range = request.GET.get('price')

    events = Event.objects.filter(is_active=True)
    if genre:
        events = events.filter(genre=genre)

    if price_range:
        filtered_events = []
        for e in events:
            p = e.min_ticket_price()
            if price_range == "free" and p == 0:
                filtered_events.append(e)
            elif price_range == "under-1000" and 0 < p < 1000:
                filtered_events.append(e)
            elif price_range == "above-1000" and p >= 1000:
                filtered_events.append(e)
        events = filtered_events

    genres = Event.GENRE_CHOICES
    return render(request, 'playlist/events.html', {
        'events': events,
        'genres': genres,
        'selected_genre': genre,
        'selected_price': price_range,
    })


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        formset = TicketOptionFormSet(request.POST, queryset=TicketOption.objects.none())

        if form.is_valid() and formset.is_valid():
            event = form.save(commit=False)
            event.is_active = False  # Require admin approval
            event.save()

            # Save ticket options
            for ticket_form in formset:
                if ticket_form.cleaned_data and not ticket_form.cleaned_data.get('DELETE', False):
                    ticket = ticket_form.save(commit=False)
                    ticket.event = event
                    ticket.save()

            return render(request, 'playlist/add_event_success.html')
    else:
        form = EventForm()
        formset = TicketOptionFormSet(queryset=TicketOption.objects.none())

    return render(request, 'playlist/add_event.html', {'form': form, 'formset': formset})




def health_check(request):
    return HttpResponse("OK", status=200)
