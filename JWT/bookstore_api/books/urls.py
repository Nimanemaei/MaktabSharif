from django.urls import path
from .views import GenerateOTPView, VerifyOTPView

urlpatterns = [
    path('otp/generate/', GenerateOTPView.as_view(), name='otp-generate'),
    path('otp/verify/', VerifyOTPView.as_view(), name='otp-verify'),
]
