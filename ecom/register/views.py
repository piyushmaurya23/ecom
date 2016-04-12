from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from ecom.events.models import Event
from .forms import RegisterForm
from .models import Register


# Create your views here.

class RegisterCreateView(CreateView):
    model = Register
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
