from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name="logout"),
    path('register/', views.register, name="register"),
    path('unregister/', views.unregister, name="unregister"),
    path('profile/', views.profile, name="profile"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
]