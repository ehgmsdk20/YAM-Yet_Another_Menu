from django.urls import path
from . import views

app_name = 'lunchmenu'

urlpatterns = [
    path('', views.index, name="index"),
]