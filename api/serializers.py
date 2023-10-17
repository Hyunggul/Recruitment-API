from rest_framework import serializers
from . import models

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recruitment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'
