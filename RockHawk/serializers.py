from rest_framework import serializers
from RockHawk.models import Feedback, LocationData


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('timestamp', 'satisfactory_level', 'comments')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Feedback.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.timestamp = validated_data.get('timestamp', instance.timestamp)
        instance.satisfactory_level = validated_data.get('satisfactory_level', instance.satisfactory_level)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.save()
        return instance

class LocationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationData
        fields = ('name', 'latitude', 'longitude', 'hotspotRadius', 'visitorCount', 'trailInfo')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return LocationData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        nstance.hotspotRadius = validated_data.get('hotspotRadius', instance.hotspotRadius)
        nstance.visitorCount = validated_data.get('visitorCount', instance.visitorCount)
        nstance.trailInfo = validated_data.get('trailInfo', instance.trailInfo)
        instance.save()
        return instance
