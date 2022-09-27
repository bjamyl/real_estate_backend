from django.urls import path
from .views import CreateInquiry,GetEnquiries


urlpatterns = [
    path('enquiries/send/', CreateInquiry.as_view(),name='Send Inquiry'),
    path('enquiries/', GetEnquiries.as_view(),name='Enquiries'),
]
