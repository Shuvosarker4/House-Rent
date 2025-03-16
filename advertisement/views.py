from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from advertisement.models import Advertisement,Review
from advertisement.serializers import AdvertisementSerializer,AdvertisementStaffSerializer,ReviewSerializer
from api.permissions import IsReviewAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class AdvertisementViewSet(ModelViewSet):
    # queryset = Advertisement.objects.filter(is_approved=True)
    # serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['category']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Advertisement.objects.all()
        return Advertisement.objects.filter(is_approved=True)
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdvertisementStaffSerializer
        return AdvertisementSerializer

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(advertisement_id=self.kwargs.get('advertisement_pk'))
    
    def get_serializer_context(self):
        return {'advertisement_id':self.kwargs.get('advertisement_pk')}