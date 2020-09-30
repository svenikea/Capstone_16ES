from django.urls import path, include
from rest_framework import routers
from rest_framework import viewsets
from .views import list_object, list_object, ShoeViewSet, ShoesBrandViewSet, detail_object, update_object
router = routers.DefaultRouter()
router.register('Shoes', ShoeViewSet)
router.register('ShoesBrand', ShoesBrandViewSet)
app_name = 'orm'
urlpatterns = [
    path('list/', list_object.as_view(), name="shoe-list"),
    path('detail/<int:pk>/', detail_object.as_view(), name="shoe-detail"),
    path('update/<int:pk>/', update_object.as_view(), name="shoe-update"),
    #path('detail/', list_object, name="Detail"),
    path('', include(router.urls)),
]
