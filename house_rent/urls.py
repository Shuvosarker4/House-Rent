from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Rent a House Api",
      default_version='v1',
      description="You can rent house by using this api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="shuvo@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/',include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



1 .   Course Mobile No : 01797451201

2 .   Result of course mobile phone no % 18 :  1

3 .   Unique Name of your project : House Rent Site

4 .   Backend Project Github  Repository  Link: https://github.com/Shuvosarker4/House-Rent

5 .   Backend Project Swagger Documentation Live  Link: https://house-rent-pied-seven.vercel.app/api/v1/

6 .   User Credential
Admin Credential 
Email: admin@admin.com
pass: 123456
Other user Credential
Email: test@gmail.com
pass: TestUser
