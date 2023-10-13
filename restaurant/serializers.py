from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Menu, Booking


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'booking_date', 'number_of_guests']


class GroupNameSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class UserSerializer(serializers.ModelSerializer):
    groups = GroupNameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'groups', 'url']
