from rest_framework import serializers

from .models import Costs


class AddCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costs
        exclude = ['user']


class GetCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costs
        fields = '__all__'
        depth = 0

