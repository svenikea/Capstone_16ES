from django.urls import path, include
from .views import ParkingLotList, ParkingList, \
    ParkingUpdate, ParkingDelete, ParkingCreate, Task_Delete, \
    LotDetail, ParkingDetail, StaffList
app_name = "alpr"
urlpatterns = [
    path('lotlist/', ParkingLotList.as_view(), name="list-all"),
    path('lotdetail/<str:pk>/', LotDetail.as_view(), name="list-detail"),
    path('list/', ParkingList.as_view(), name="parking-list"),
    path('update/<str:pk>/', ParkingUpdate.as_view(), name="parking-update"),
    path('delete/<str:pk>/', ParkingDelete.as_view(), name="parking-delete"),
    path('del/<str:pk>/', Task_Delete, name="del"),
    path('new/', ParkingCreate.as_view(), name="parking-create"),
    path('details/<str:pk>/', ParkingDetail.as_view(), name="parking-detail"),
    path('staffs/', StaffList.as_view(), name="staff-list"),
]
