from realtors.models import Realtor
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RealtorSerializer
from django.http import Http404


class RealtorAV(APIView):
    def get(self, request):
        realtors = Realtor.objects.all()
        serializer = RealtorSerializer(realtors, many=True)
        return Response(serializer.data)
    
    
    
class RealtorDetail(APIView):
    def get(self,request, pk,):
        try:
            realtor = Realtor.objects.get(pk=pk)
        except Realtor.DoesNotExist:
            raise Http404
        serializer = RealtorSerializer(realtor)
        return Response(serializer.data)

        
        