from django.urls import path
from .views import ReplyList, ReplyDetail

urlpatterns = [
    path('', ReplyList.as_view(), name='reply-list'),  
    path('<int:pk>/', ReplyDetail.as_view(), name='reply-detail'),  
]
