from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from advertisement.models import Advertisement
from advertisement.serializers import AdvertisementSerializer
from api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class AdvertisementViewSet(ModelViewSet):
    # queryset = Advertisement.objects.filter(is_approved=True)
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['category']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Advertisement.objects.all()
        return Advertisement.objects.filter(is_approved=True)

