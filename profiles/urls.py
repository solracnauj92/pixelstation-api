from django.urls import path
from . import views


urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile-list'),
    path('<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
]


