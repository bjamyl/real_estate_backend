from xml.dom.minidom import Document
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.api.urls')),
    path('api/', include('realtors.api.urls')),
    path('api/', include('accounts.api.urls')),
    path('api/', include('enquiries.api.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 
