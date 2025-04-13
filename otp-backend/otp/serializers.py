from rest_framework import serializers
from .models import OTP

class OtpListSerializer(serializers.ModelSerializer):
    expired = serializers.SerializerMethodField()


    class Meta:
        model = OTP
        exclude = ['password', 'created_at', "expires_at"]  # ou fields = ['id', 'expires_at', 'used']

    def get_expired(self, obj):
        from django.utils import timezone
        return timezone.now() > obj.expires_at



class OtpDetailSerializer(serializers.ModelSerializer):
    expired = serializers.SerializerMethodField()

    class Meta:
        model = OTP
        fields = '__all__'
        # exemple : fields = ['id', 'password', 'expires_at', 'used', 'expired']

    def get_expired(self, obj):
        from django.utils import timezone
        return timezone.now() > obj.expires_at
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        is_expired = self.get_expired(instance)
        if instance.used or is_expired:
            rep['password'] = None  # ou `del rep['password']` pour le supprimer complètement

        return rep
