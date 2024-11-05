from django.urls import path
from .views import HubList, HubDebateList, DebateDetail

urlpatterns = [
    path('hubs/', HubList.as_view(), name='hub-list'),                    # List and create hubs
    path('hubs/<int:hub_id>/debates/', HubDebateList.as_view(), name='hub-debate-list'),  # List/create debates in a hub
    path('hubs/<int:hub_id>/debates/<int:pk>/', DebateDetail.as_view(), name='debate-detail'),   # Retrieve, update, delete a specific debate
]
