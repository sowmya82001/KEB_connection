from django.urls import path
from .forms import CaptchaLoginForm
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home_view, name='home'),
    path('apply/', views.apply_connection, name='apply_connection'),
    path('connections/', views.connection_list, name='connection_list'),
    path('contact/', views.contact, name='contact'),
    path('forget-password/', views.forget_password_view, name='forget_password'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('login/', auth_views.LoginView.as_view(form_class=CaptchaLoginForm), name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
