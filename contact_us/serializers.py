from rest_framework import serializers
from .import models

class ConatactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.ContactUs
        fields='__all__'
    