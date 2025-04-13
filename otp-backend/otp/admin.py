from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import OTP

@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'expires_at', 'used')
    list_filter = ('used',)
    search_fields = ('id',)
