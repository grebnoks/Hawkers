from rest_framework import serializers
from RockHawk.models import Feedback, LocationData, TrailData


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('timestamp', 'satisfactory_level', 'comments', 'name', 'email', 'phone_number')

    def create(self, validated_data):
        """
        Create and return a new `Feedback` instance, given the validated data.
        """
        return Feedback.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Feedback` instance, given the validated data.
        """
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.satisfactory_level = validated_data.get('satisfactory_level', instance.satisfactory_level)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()
        return instance

class LocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = ('id', 'picture', 'name', 'latitude', 'longitude', 'hotspot_radius', 'visitor_count', 'hotspot_info', 'location_type')

    def create(self, validated_data):
        """
        Create and return a new `LocationData` instance, given the validated data.
        """
        return LocationData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `LocationData` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        nstance.picture = validated_data.get('picture', instance.picture)
        instance.name = validated_data.get('name', instance.name)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.hotspot_radius = validated_data.get('hotspot_radius', instance.hotspot_radius)
        instance.visitor_count = validated_data.get('visitor_count', instance.visitor_count)
        instance.hotspot_info = validated_data.get('hotspot_info', instance.hotspot_info)
        instance.location_type = validated_data.get('location_type', instance.location_type)
        instance.save()
        return instance

class TrailDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrailData
        fields = ('id', 'name', 'trail_info', 'trail_length_in_miles', 'trail_latitudes', 'trail_longitudes', 'trail_type', 'trail_color')

    def create(self, validated_data):
        """
        Create and return a new `TrailData` instance, given the validated data.
        """
        return TrailData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TrailData` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.trail_info = validated_data.get('trail_info', instance.trail_info)
        instance.trail_length_in_miles = validated_data.get('trail_length_in_miles', instance.trail_length_in_miles)
        instance.trail_latitudes = validated_data.get('trail_latitudes', instance.trail_latitudes)
        nstance.trail_longitudes = validated_data.get('trail_longitudes', instance.trail_longitudes)
        instance.trail_type = validated_data.get('trail_type', instance.trail_type)
        instance.trail_color = validated_data.get('trail_color', instance.trail_color)
        instance.save()
        return instance

