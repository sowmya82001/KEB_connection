from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply_connection, name='apply_connection'),
    path('connections/', views.connection_list, name='connection_list'),
    path('contact/', views.contact, name='contact'),
]
