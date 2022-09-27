from .serializers import EnquiriesSerializer
from enquiries.models import Enquirie
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

        
        
class CreateInquiry(APIView):
    def post(self, request):
        serializer = EnquiriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

class GetEnquiries(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        enquiries = Enquirie.objects.order_by('-inquiry_date').filter(user_id=user.id)
        serializer = EnquiriesSerializer(enquiries, many=True)
        return Response(serializer.data)
        