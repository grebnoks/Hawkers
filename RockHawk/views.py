from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from RockHawk.models import Feedback, LocationData
from RockHawk.serializers import FeedbackSerializer, LocationDataSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponseRedirect, HttpRequest
from django.utils import timezone


@api_view(['GET', 'POST'])
def feedback_list(request, format=None):
    if request.method == 'GET':
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def feedback_detail(request, pk, format=None):
    try:
        feedback = Feedback.objects.get(pk=pk)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def locationData_list(request, format=None):
    if request.method == 'GET':
        locationData = LocationData.objects.all()
        serializer = LocationDataSerializer(locationData, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def locationData_detail(request, pk, format=None):
    try:
        locationData = LocationData.objects.get(pk=pk)
    except LocationData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationDataSerializer(locationData)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LocationDataSerializer(locationData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = LocationDataSerializer(locationData.visitorCount, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        locationData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
