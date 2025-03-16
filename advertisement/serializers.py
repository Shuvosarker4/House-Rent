from rest_framework import serializers
from advertisement.models import Advertisement
from advertisement.models import Review
from django.contrib.auth import get_user_model

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'user', 'title', 'description', 'category', 'price', 'location', 'is_approved', 'created_at']
        read_only_fields =['is_approved']

class AdvertisementStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'user', 'title', 'description', 'category', 'price', 'location', 'is_approved', 'created_at']


class SimpleUserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name='get_current_user_name')
    class Meta:
        model = get_user_model()
        fields = ['id','name']

    def get_current_user_name(self,obj):
        return obj.get_full_name()

class ReviewSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id','user','advertisement','ratings','comment']
        read_only_fields = ['user','advertisement']
    
    def create(self, validated_data):
        advertisement_id = self.context['advertisement_id']
        return Review.objects.create(advertisement_id=advertisement_id,**validated_data)
