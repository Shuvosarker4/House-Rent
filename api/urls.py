from django.urls import path,include
from rest_framework_nested import routers
from advertisement.views import AdvertisementViewSet

router = routers.DefaultRouter()
router.register('advertisements',AdvertisementViewSet,basename='advertisement-list')


urlpatterns = [
    path('',include(router.urls)),
]