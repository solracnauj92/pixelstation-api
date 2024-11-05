from django.urls import path
from .views import HubList, DebateList, DebateDetail, ResponseList, ResponseDetail

urlpatterns = [
    path('hubs/', HubList.as_view(), name='hub-list'),
    path('debates/', DebateList.as_view(), name='debate-list'),
    path('debates/<int:pk>/', DebateDetail.as_view(), name='debate-detail'),
    path('responses/', ResponseList.as_view(), name='response-list'),
    path('responses/<int:pk>/', ResponseDetail.as_view(), name='response-detail'),
]
