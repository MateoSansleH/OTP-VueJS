from django.urls import path
from .views import OTPListCreateView, OTPDetailView

urlpatterns = [
    path('otp/', OTPListCreateView.as_view(), name='otp-list-create'),
    path('otp/<uuid:id>/', OTPDetailView.as_view(), name='otp-detail'),
]
