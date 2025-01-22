from rest_framework import serializers
from .models import ParentUser, ChildUser

class ParentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentUser
        fields = 'all'
        read_only_fields = ['created_at', 'updated_at', 'id']

class ChildUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildUser
        fields = 'all'
        read_only_fields = ['created_at', 'updated_at', 'id']