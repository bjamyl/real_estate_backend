from rest_framework import serializers
from listings.models import Listing


class ListingsSerializer(serializers.ModelSerializer):
    realtor = serializers.CharField(source='realtor.name')
    class Meta:
        model = Listing
        fields = '__all__'