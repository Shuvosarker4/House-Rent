from django.urls import path,include
from rest_framework_nested import routers
from advertisement.views import AdvertisementViewSet,ReviewViewSet,SavingFavoritesViewSet
from rentRequest.views import RentRequestViewSet
router = routers.DefaultRouter()
router.register('advertisements',AdvertisementViewSet,basename='advertisement-list')
router.register('rent_requests',RentRequestViewSet,basename='rent-list')


ad_router = routers.NestedDefaultRouter(router,'advertisements',lookup = 'advertisement')
ad_router.register('reviews',ReviewViewSet,basename='advertisement-review')
ad_router.register('saving_favorites',SavingFavoritesViewSet,basename='advertisement-favorites')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(ad_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]