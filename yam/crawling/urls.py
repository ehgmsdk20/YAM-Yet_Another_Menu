from django.urls import path
from . import views

app_name = 'crawling'

urlpatterns = [
    path('result/<str:rest_list>/', views.result, name="result"),

]