from django.urls import path,include
from rest_framework_nested import routers
from advertisement.views import AdvertisementViewSet,ReviewViewSet
from rentRequest.views import RentRequestViewSet
router = routers.DefaultRouter()
router.register('advertisements',AdvertisementViewSet,basename='advertisement-list')
router.register('rent_requests',RentRequestViewSet,basename='rent-list')


product_router = routers.NestedDefaultRouter(router,'advertisements',lookup = 'advertisement')
product_router.register('reviews',ReviewViewSet,basename='advertisement-review')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(product_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]