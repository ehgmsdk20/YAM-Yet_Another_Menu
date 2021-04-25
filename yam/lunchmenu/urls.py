from django.urls import path
from . import views

app_name = 'lunchmenu'

urlpatterns = [
    path('', views.index, name="index"),
    path('information/', views.information, name = 'information'),
    path('result/<str:lat>/<str:lng>/', views.result, name = 'result'),
]