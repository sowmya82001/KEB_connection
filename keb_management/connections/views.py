from django.shortcuts import render, redirect
from .models import Customer, Connection
from .forms import CustomerForm, ConnectionForm, ContactForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from django.contrib.auth.models import User
from .models import OTPStorage
from django.core.mail import send_mail
import random
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponse

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

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Use the new form with CAPTCHA
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/home/')
        else:
            messages.error(request, "Invalid credentials or CAPTCHA, please try again.")
    else:
        form = LoginForm()  # Use the new form with CAPTCHA

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def forget_password_view(request):
    if request.method == 'POST':
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            users = User.objects.filter(email=email)

            if users.exists():
                user = users.first()  # Take the first matching user
                otp = str(random.randint(100000, 999999))
                OTPStorage.objects.update_or_create(user=user, defaults={'otp': otp})
                send_mail(
                    'Your OTP Code',
                    f'Your OTP code is {otp}',
                    'admin@example.com',
                    [email],
                    fail_silently=False,
                )
                request.session['reset_email'] = email
                return redirect('reset_password')
            else:
                form.add_error('email', 'Email not found.')
    else:
        form = ForgetPasswordForm()
    return render(request, 'forget_password.html', {'form': form})

def reset_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = request.session.get('reset_email')
            otp_entered = form.cleaned_data['otp']
            new_password = form.cleaned_data['new_password']

            user = User.objects.filter(email=email).first()  # safer than get()
            if not user:
                form.add_error(None, 'User not found.')
            else:
                otp_record = OTPStorage.objects.filter(user=user, otp=otp_entered).first()
                if otp_record:
                    user.set_password(new_password)
                    user.save()
                    del request.session['reset_email']
                    return redirect('login')  # Or wherever you want
                else:
                    form.add_error('otp', 'Invalid OTP.')
    else:
        form = ResetPasswordForm()
    return render(request, 'reset_password.html', {'form': form})


def home_view(request):
    return render(request, 'connections/home.html')

def logout_user(request):
    logout(request)
    return redirect('/')