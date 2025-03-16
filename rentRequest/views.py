from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rentRequest.models import RentRequest
from rentRequest.serializers import RentRequestSerializer
# Create your views here.

class RentRequestViewSet(ModelViewSet):
    queryset = RentRequest.objects.all()
    serializer_class = RentRequestSerializer
