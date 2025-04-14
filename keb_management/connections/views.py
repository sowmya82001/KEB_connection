from django.shortcuts import render, redirect
from .models import Customer, Connection
from .forms import CustomerForm, ConnectionForm, ContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

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

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists. Please choose another one.")
                return render(request, 'register.html', {'form': form})

            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')