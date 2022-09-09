from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListingsSerializer
from listings.models import Listing
from django.http import Http404


class ListingsView(APIView):
    def get(self, request):
        listings = Listing.objects.all()
        serializer = ListingsSerializer(listings, many=True)
        return Response(serializer.data)
    

class ListingDetail(APIView):
    def get(self,request,pk):
        try:
            listing = Listing.objects.get(pk=pk) 
        except Listing.DoesNotExist:
            raise Http404 
        serializer = ListingsSerializer(listing)
        return Response(serializer.data)
    
        