from django import forms
from .models import Customer, Connection, ContactMessage
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ConnectionForm(forms.ModelForm):
    class Meta:
        model = Connection
        fields = ['customer', 'connection_type']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

class CaptchaLoginForm(AuthenticationForm):
    captcha = CaptchaField()

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(AuthenticationForm):
    captcha = CaptchaField()

class ForgetPasswordForm(forms.Form):
    email = forms.EmailField()

class ResetPasswordForm(forms.Form):
    otp = forms.CharField(max_length=6)
    new_password = forms.CharField(widget=forms.PasswordInput)
