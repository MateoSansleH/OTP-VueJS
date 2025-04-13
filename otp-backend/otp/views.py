from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import OTP
from .serializers import OTPSerializer


from django.utils import timezone
from datetime import timedelta

class OTPListCreateView(generics.ListCreateAPIView):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer

class OTPDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.used:
            return Response({"error": "OTP déjà utilisé."}, status=status.HTTP_410_GONE)

        if timezone.now() > instance.expires_at:
            return Response({"error": "OTP expiré."}, status=status.HTTP_410_GONE)

        instance.used = True
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
