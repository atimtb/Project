from django.shortcuts import render



from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status


@api_view(['GET'])
def home(request):
    return Response("this is home")