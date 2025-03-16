from rest_framework import serializers
from rentRequest.models import RentRequest

class RentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentRequest
        fields = ['id', 'user', 'advertisement', 'status', 'created_at']