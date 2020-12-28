from rest_framework import serializers
from .models import Parking, Parkinglotlist, Stafflist, Cameralist, History

# Child


class ParkingSerializer(serializers.ModelSerializer):
    # class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    # parkinglotid_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Parkinglotlist.objects.all(),
    #     source='parkinglotid.id',

    # )
    # view_name = "alpr:parkinglotlist-detail"

    class Meta:
        model = Parking
        fields = '__all__'

    # def create(self, validated_data):
    #     subject = Parking.objects.create(
    #         parkinglotid=validated_data['parkinglotid']['id'], rfid=validated_data['rfid'],
    #         platenumber=validated_data['platenumber'],
    #         plateimgurl=validated_data['plateimgurl'],
    #         checkintime=validated_data['checkintime']
    #     )
    #     return output

# Master


class ParkinglotlistSerializer(serializers.ModelSerializer):
    # class ParkinglotlistSerializer(serializers.HyperlinkedModelSerializer):
    # parking = ParkingSerializer(many=True, read_only=True)
    # view_name = "alpr:parking-detail"

    class Meta:
        model = Parkinglotlist
        fields = '__all__'


class StafflistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stafflist
        fields = '__all__'


class CameralistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cameralist
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
