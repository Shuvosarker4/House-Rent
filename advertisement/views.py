from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from advertisement.models import Advertisement,Review,SavingFavorites
from advertisement.serializers import AdvertisementSerializer,AdvertisementStaffSerializer,ReviewSerializer,SavingFavoritesSerializer
from api.permissions import IsReviewAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from sslcommerz_lib import SSLCOMMERZ 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
# Create your views here.

class AdvertisementViewSet(ModelViewSet):
    permission_classes = [IsReviewAuthorOrReadOnly,IsAuthenticatedOrReadOnly]
    filter_backends =[DjangoFilterBackend]
    # filterset_fields = ['category','is_approved']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Advertisement.objects.all()
        return Advertisement.objects.filter(is_approved=True)
    
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return AdvertisementStaffSerializer
        return AdvertisementSerializer
    
    @property
    def filterset_fields(self):
        if self.request.user.is_staff:
            return ['category', 'is_approved']
        return ['category']

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
    

class SavingFavoritesViewSet(ModelViewSet):
    serializer_class = SavingFavoritesSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return SavingFavorites.objects.filter(advertisement_id=self.kwargs.get('advertisement_pk'))
    
    def get_serializer_context(self):
        return {'advertisement_id':self.kwargs.get('advertisement_pk')}
    

@api_view(['POST'])
def initiate_payment(request):
    user = request.user
    amount = request.data.get('amount')
    settings = { 'store_id': 'house682b1552b2320', 'store_pass': 'house682b1552b2320@ssl', 'issandbox': True }
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "12345"
    post_body['success_url'] = "https://house-rent-client-tau.vercel.app/payment/success"
    post_body['fail_url'] = "your fail url"
    post_body['cancel_url'] = "your cancel url"
    post_body['emi_option'] = 0
    post_body['cus_name'] = f"{user.first_name}"
    post_body['cus_email'] = user.email
    post_body['cus_phone'] = user.email
    post_body['cus_add1'] = user.email
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Property Rent"
    post_body['product_category'] = "Rent Property"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) # API response
    print(response)
    if response.get('status') == 'SUCCESS':
        return Response({"payment_url": response.get('GatewayPageURL')}, status=status.HTTP_200_OK)
    return Response({"error": "Failed to initiate payment"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def payment_success(request):
    return redirect("https://house-rent-client-tau.vercel.app/payment/success")