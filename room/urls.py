from django.urls import path
from .views import RoomView , RoomTypeView ,RoomDistrictView ,RoomStatusView , RoomDetailView


urlpatterns = [
    path('room/', RoomView.as_view()),
    path('room-type/', RoomTypeView.as_view()),
    path('districts/', RoomDistrictView.as_view()),
    path('room-status/', RoomStatusView.as_view()),
    path('room/<int:pk>/',RoomDetailView.as_view()),
]
