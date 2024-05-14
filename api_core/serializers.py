from rest_framework import serializers
from .models import medicines



class medicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicines
        exclude = ['id']