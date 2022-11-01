from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListingsSerializer
from listings.models import Listing
from django.http import Http404
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ListingsView(APIView):
    def get(self,):
        listings = Listing.objects.all()
        serializer = ListingsSerializer(listings, many=True)
        return Response(serializer.data)
    

class Listings(generics.ListAPIView):
    serializer_class = ListingsSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['address','city', 'description']
    filterset_fields = ['region',]
    
    def get_queryset(self):
        queryset=Listing.objects.all()
        bedrooms = self.request.query_params.get('bedrooms')
        price = self.request.query_params.get('price')
        
        if bedrooms: #Checking if key is not none
            queryset=queryset.filter(bedrooms__lte=bedrooms)
        
        if price: #Checking if key is not none
            queryset=queryset.filter(price__lte=price)
        return queryset

class ListingDetail(APIView):
    def get(self,request,pk):
        try:
            listing = Listing.objects.get(pk=pk) 
        except Listing.DoesNotExist:
            raise Http404 
        serializer = ListingsSerializer(listing)
        return Response(serializer.data)
    
        