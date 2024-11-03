from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.ProfileList.as_view()),  # Now accessible at /profiles/
    path('<int:pk>/', views.ProfileDetail.as_view()),  # Accessible at /profiles/<id>/
]

