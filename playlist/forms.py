from django import forms
from django.forms import modelformset_factory
from .models import Event, TicketOption
from datetime import datetime


class EventForm(forms.ModelForm):
    event_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True,
        label="Event Date"
    )
    event_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        required=True,
        label="Event Time"
    )

    class Meta:
        model = Event
        fields = ['name', 'genre', 'custom_genre', 'venue', 'description', 'ticket_link', 'image_url']
    
    def clean(self):
        cleaned_data = super().clean()
        genre = cleaned_data.get('genre')
        custom_genre = cleaned_data.get('custom_genre')

        if genre == 'other' and not custom_genre:
            self.add_error('custom_genre', 'Please specify the event type if you select Other.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # combine date + time into datetime
        date = self.cleaned_data.get('event_date')
        time = self.cleaned_data.get('event_time')
        if date and time:
            instance.date = datetime.combine(date, time)
        if commit:
            instance.save()
        return instance


# Form for ticket options
class TicketOptionForm(forms.ModelForm):
    class Meta:
        model = TicketOption
        fields = ['label', 'price']
        widgets = {
            'label': forms.TextInput(attrs={'placeholder': 'e.g. VIP, Regular, Early Bird'}),
            'price': forms.TextInput(attrs={'placeholder': 'e.g. Free, Ksh 500, Ksh 2000'}),
        }


# Formset (allows multiple ticket options)
TicketOptionFormSet = modelformset_factory(
    TicketOption,
    form=TicketOptionForm,
    extra=1,
    can_delete=True
)
