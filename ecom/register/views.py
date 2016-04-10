from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .forms import RegisterForm
from .models import Register
from ecom.events.models import Event


# Create your views here.

class RegisterCreateView(CreateView):
    model = Register
    form_class = RegisterForm

    class ResumeCreateView(CreateView):
        form_class = RegisterForm
        model = Register

        def form_valid(self, form):
            form.instance.event = Event.objects.get(pk=self.request.pk)
            return super(RegisterCreateView, self).form_valid(form)



def thanks(request, pk=None):
    instance = get_object_or_404(Register, pk=pk)
    context = {
        "user": instance.name,
        "email": instance.email
    }

    return render(request, "register/thanks.html", context)
