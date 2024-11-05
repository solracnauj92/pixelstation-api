from django.urls import path
from .views import HubList, HubDebateList, DebateDetail

urlpatterns = [
    path('hubs/', HubList.as_view(), name='hub-list'),
    path('hubs/<int:hub_id>/debates/', HubDebateList.as_view(), name='hub-debate-list'),
    path('hubs/<int:hub_id>/debates/<int:pk>/', DebateDetail.as_view(), name='debate-detail'),
]
