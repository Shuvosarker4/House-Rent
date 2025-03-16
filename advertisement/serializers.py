from rest_framework import serializers
from advertisement.models import Advertisement

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'user', 'title', 'description', 'category', 'price', 'location', 'is_approved', 'created_at']