# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.subscribe, name='subscribe'),  
    path('validate/', views.validate_email, name='validate_email'),
]
