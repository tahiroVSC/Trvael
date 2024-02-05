from rest_framework import serializers

from apps.tours.models import Tour
from apps.hotels.serializers import HotelSerializer


class TourSerializers(serializers.ModelSerializer):
    tour_hotels = HotelSerializer(read_only=True, many=True)
    class Meta:
        model = Tour 
        fields = "__all__"