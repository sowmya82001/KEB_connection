from django import forms
from .models import Customer, Connection, ContactMessage

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