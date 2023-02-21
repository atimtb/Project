from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from .serializers import AddCostSerializer, GetCostSerializer

from users.models import Profile, Family
from managing.models import Costs


@api_view(['POST'])
def add_cost(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return Response({"message":"profile does not exists"}, status=status.HTTP_404_NOT_FOUND)
    serializer = AddCostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['user'] = profile
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_cost(requset):

    user = requset.user
    profile = Profile.objects.get(user=user)
    costs = Costs.objects.filter(user=profile)
    total = 0
    for cost in costs:
        spent = cost.cost
        total = total + spent

    serializer = GetCostSerializer(costs, many=True)
    return Response({"total":total, "data": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_family_cost(requset):

    user = requset.user
    try:
        profile = Profile.objects.get(user=user)
    except TypeError:
        return Response({"message":"you are not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    if profile.has_a_family == True:
        family=profile.family
        members = Profile.objects.filter(family=family)
        total = 0
        total_costs = []
        for member in members:
            costs = Costs.objects.filter(user = member)
            for cost in costs:
                total_costs.append(cost)
                spent = cost.cost
                total = total + spent
            
        serializer = GetCostSerializer(total_costs, many=True)
        return Response({"total":total, "data":serializer.data}, status=status.HTTP_200_OK)

    else:
        return Response({"message":"you are not a member of any families"})




