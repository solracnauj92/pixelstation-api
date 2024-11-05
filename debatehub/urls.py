from django.urls import path
from .views import HubList, DebateList, DebateDetail, ResponseList, ResponseDetail

urlpatterns = [
    path('hubs/', HubList.as_view(), name='hub-list'),                   # List and create hubs
    path('debates/', DebateList.as_view(), name='debate-list'),         # List and create debates
    path('debates/<int:pk>/', DebateDetail.as_view(), name='debate-detail'),  # Retrieve, update, delete a specific debate
    path('responses/', ResponseList.as_view(), name='response-list'),     # List and create responses
    path('responses/<int:pk>/', ResponseDetail.as_view(), name='response-detail'),  # Retrieve, update, delete a specific response
]

