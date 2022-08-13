from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistrationForm

# Create your views here.
#class RegistrationView(CreateView):
    #model = User
    #form_class = RegistrationForm
    #template_name = 'registration/register.html'
    #success_url = reverse_lazy('login')


def registrationview(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form':form})

