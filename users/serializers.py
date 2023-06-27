from rest_framework import serializers

from .models import User, Profile , Family

class ViewMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

        def create(self, validated_data):
            return User.objects.create_user(**validated_data)


class ViewProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']


class ViewFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

