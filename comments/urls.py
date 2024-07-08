from django.urls import path
from comments import views

urlpatterns = [
    path('', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
]