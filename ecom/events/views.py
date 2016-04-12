from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

from braces.views import LoginRequiredMixin

from .models import Event

# Create your views here.

class EventListView(ListView):
    modal = Event
    queryset = Event.objects.all()


class EventDetailView(DetailView):
    model = Event



class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = [
        'title',
        'description',
        'price',
        'image',
        'organiser',
        'venue'
    ]
