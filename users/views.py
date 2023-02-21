from django.shortcuts import render

from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status



class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


@api_view(['GET'])
def view_profile(request):
    user = request.user

    try:
        this_user = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return Response({"message":"this profile does not exists."}, status=status.HTTP_404_NOT_FOUND)

    serializer = ViewProfileSerializer(this_user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_profile(request):
    
    user = request.user

    serializer = CreateProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['user'] = user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ViewFamily(generics.ListAPIView):
    serializer_class = ViewFamilySerializer
    queryset = Family.objects.filter(name='e-family')




