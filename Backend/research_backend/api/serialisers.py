from django.contrib.auth.models import User
from .models import Research
from rest_framework import serializers

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extras = {'paswword': {'write_only': True}}
    
    def create(self, verified_data):
        user = User.objects.create_user(**verified_data)
        return user
    

class ResearchSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = ['id', 'topic', 'research_papers', 'research_date', 'researcher']
        extras = {'researcher': {'read_only': True}}
    