from rest_framework import serializers

from app_core.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"