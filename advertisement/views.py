from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from advertisement.models import Advertisement
from advertisement.serializers import AdvertisementSerializer
from api.permissions import IsAdminOrReadOnly
# Create your views here.

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAdminOrReadOnly]

