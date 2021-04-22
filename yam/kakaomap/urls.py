from . import views
from django.urls import path

app_name = 'kakaomap'

urlpatterns = [
    path('searchaddr/<slug:input_id>/', views.searchaddr, name="searchaddr"),
]