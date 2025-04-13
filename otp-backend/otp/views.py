from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import OTP
from .serializers import OTPSerializer

class OTPListCreateView(generics.ListCreateAPIView):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer

class OTPDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer
    lookup_field = 'id'
