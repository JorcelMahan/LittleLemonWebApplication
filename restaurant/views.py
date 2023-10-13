from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Menu, Booking
from django.core import serializers
from .models import Booking
from .serializers import MenuSerializer, BookingSerializer
from datetime import datetime

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Page views


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def reservations(request: HttpRequest) -> HttpResponse:
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": booking_json})


# API views


class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
