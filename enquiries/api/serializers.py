from rest_framework.serializers import ModelSerializer
from enquiries.models import Enquirie

class EnquiriesSerializer(ModelSerializer):
    class Meta:
        model = Enquirie
        fields = '__all__'