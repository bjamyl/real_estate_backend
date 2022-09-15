from django.urls import path
from realtors.api.views import RealtorAV, RealtorDetail

urlpatterns = [
    path('realtors/', RealtorAV.as_view(), name='realtor-list'),
    path('realtors/<int:pk>', RealtorDetail.as_view(), name='realtor-detail'),
]
