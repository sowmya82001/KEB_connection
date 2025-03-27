from django.shortcuts import render, redirect
from .models import Customer, Connection
from .forms import CustomerForm, ConnectionForm, ContactForm

def home(request):
    return render(request, 'connections/home.html')

def apply_connection(request):
    if request.method == 'POST':
        form = ConnectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ConnectionForm()
    return render(request, 'connections/apply_connection.html', {'form': form})

def connection_list(request):
    connections = Connection.objects.all()
    return render(request, 'connections/connection_list.html', {'connections': connections})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'connections/contact.html', {'form': form})