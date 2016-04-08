from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import Register
from ecom.events.models import Event

# Create your views here.

class RegisterCreateView(CreateView):
    model = Register
    event = Event.pk
    fields = [
        'event',
        'name',
        'email',
        'mobile',
    ]



def thanks(request, pk=None):
    instance = get_object_or_404(Register, pk=pk)
    context = {
        "user": instance.name,
        "email": instance.email
    }

    return render(request, "register/thanks.html", context)
