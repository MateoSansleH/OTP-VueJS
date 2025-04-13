from rest_framework import serializers
from .models import OTP

class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # évite l'affichage dans les listes
        }