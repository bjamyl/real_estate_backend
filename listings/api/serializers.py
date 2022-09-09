from rest_framework import serializers
from listings.models import Listing


class ListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'