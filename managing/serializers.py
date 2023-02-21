from rest_framework import serializers

from .models import Costs


class AddCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costs
        exclude = ['user']


class GetCostSerializer(serializers.ModelSerializer):
    # total_cost = serializers.FloatField()

    class Meta:
        model = Costs
        fields = '__all__'
        depth = 0

