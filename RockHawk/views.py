from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from RockHawk.models import Feedback, LocationData, TrailData #Make sure to add any new Models here
from RockHawk.serializers import FeedbackSerializer, LocationDataSerializer, TrailDataSerializer #Make sure to add any new Serializers here
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from django.utils import timezone

#This file pertains to the views which repsond to API requests. You will notice that there are 3 pairs. Each pair has an API that deals with the list, and another API that deals with spcific records.

#This API can only handle GET and POST requests and deals with the list of all the feedback objects in the database
@api_view(['GET', 'POST'])
def feedback_list(request, format=None):
    #Handles a GET request and will return all the feedback data in the list
    if request.method == 'GET':
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True) #Uses a serializer to obtain data
        return Response(serializer.data)

    #Handles a POST request
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedbackSerializer(data=data) #Uses a serializer to create/save brand new data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #Succesful API response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Failed API response

#This API can only handle GET, PUT, and DELETE requests on specific records in the database pertaining to feedback
@api_view(['GET', 'PUT', 'DELETE'])
def feedback_detail(request, pk, format=None):
    try:
        feedback = Feedback.objects.get(pk=pk)
    except Feedback.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Failed API response

    #Handles a GET request
    if request.method == 'GET':
        serializer = FeedbackSerializer(feedback) #Uses a serializer to obtain data
        return Response(serializer.data)

    #Handles a PUT request
    elif request.method == 'PUT':
        serializer = FeedbackSerializer(feedback, data=request.data) #Uses a serializer to cupdate existing data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Failed API response

    #Handles a DELETE request
    elif request.method == 'DELETE':
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)#Succesful API response

#This API can only handle GET and POST requests and deals with the list of all the location data objects in the database
@api_view(['GET', 'POST'])
def locationData_list(request, format=None):
    #Handles a GET request and will return all the location data data in the list
    if request.method == 'GET':
        locationData = LocationData.objects.all()
        serializer = LocationDataSerializer(locationData, many=True) #Uses a serializer to obtain data
        return Response(serializer.data)

    #Handles a POST request
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationDataSerializer(data=data) #Uses a serializer to create/save brand new data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)#Succesful API response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Failed API response

#This API can only handle GET, PUT, and DELETE requests on specific records in the database pertaining to location data
@api_view(['GET', 'PUT', 'DELETE'])
def locationData_detail(request, pk, format=None):
    try:
        locationData = LocationData.objects.get(pk=pk)
    except LocationData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Failed API response

    #Handles a GET request
    if request.method == 'GET':
        serializer = LocationDataSerializer(locationData) #Uses a serializer to obtain data
        return Response(serializer.data)

    #Handles a PUT request
    elif request.method == 'PUT':
        serializer = LocationDataSerializer(locationData, data=request.data) #Uses a serializer to cupdate existing data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Failed API response

    #Handles a DELETE request
    elif request.method == 'DELETE':
        locationData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)#Succesful API response

#This API can only handle GET and POST requests and deals with the list of all the trail objects in the database
@api_view(['GET', 'POST'])
def trailData_list(request, format=None):
    #Handles a GET request and will return all the trail data in the list
    if request.method == 'GET':
        trailData = TrailData.objects.all()
        serializer = TrailDataSerializer(trailData, many=True) #Uses a serializer to obtain data
        return Response(serializer.data)

    #Handles a POST request
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TrailDataSerializer(data=data) #Uses a serializer to create/save brand new data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)#Succesful API response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Failed API response

#This API can only handle GET, PUT, and DELETE requests on specific records in the database pertaining to trails
@api_view(['GET', 'PUT', 'DELETE'])
def trailData_detail(request, pk, format=None):
    try:
        trailData = TrailData.objects.get(pk=pk)
    except TrailData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)#Failed API response

    #Handles a GET request
    if request.method == 'GET':
        serializer = TrailDataSerializer(trailData) #Uses a serializer to obtain data
        return Response(serializer.data)

    #Handles a PUT request
    elif request.method == 'PUT':
        serializer = TrailDataSerializer(trailData, data=request.data) #Uses a serializer to cupdate existing data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)#Failed API response

    #Handles a DELETE request
    elif request.method == 'DELETE':
        trailData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)#Succesful API response
