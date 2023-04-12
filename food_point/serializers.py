import json

from rest_framework import serializers
from food_point.models import Printer, Check


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = '__all__'

    # def validate(self, attrs):
    #     order = attrs.get("order")
    #     if Check.objects.filter(order=order).exists():
    #         raise serializers.ValidationError("An order has already exists")
    #     return attrs
