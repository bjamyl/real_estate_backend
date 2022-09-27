from django.urls import path
from listings.api.views import ListingsView, ListingDetail, Listings

urlpatterns = [
    # path('listings/', ListingsView.as_view(), name='listings'),
    path('listings/<int:pk>', ListingDetail.as_view(), name='listing-detail'),
    path('listings/', Listings.as_view(), name='all-listings'),
]
