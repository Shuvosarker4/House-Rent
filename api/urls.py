from django.urls import path,include
from rest_framework_nested import routers
from advertisement.views import AdvertisementViewSet
from rentRequest.views import RentRequestViewSet
router = routers.DefaultRouter()
router.register('advertisements',AdvertisementViewSet,basename='advertisement-list')
router.register('rent_requests',RentRequestViewSet,basename='rent-list')


urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]