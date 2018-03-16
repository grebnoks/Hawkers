from rest_framework import serializers
from polls.models import Student, Feedback


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('major', 'name', 'age')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.major = validated_data.get('major', instance.major)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

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
