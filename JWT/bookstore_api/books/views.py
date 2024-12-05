import random
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class GenerateOTPView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user, created = User.objects.get_or_create(phone_number=phone_number)
        
        # Generate a random OTP
        otp = random.randint(100000, 999999)  # Replace with a real OTP generator in production
        
        # Send OTP via SMS (pseudo-code)
        print(f"OTP for {phone_number}: {otp}")  # Replace this with actual SMS sending logic
        
        # Store OTP in session for demo purposes
        request.session[f'otp_{phone_number}'] = otp  
        
        return Response({"message": "OTP sent to phone number."})

class VerifyOTPView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')
        saved_otp = request.session.get(f'otp_{phone_number}')
        
        if str(otp) == str(saved_otp):
            user = User.objects.get(phone_number=phone_number)
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            })
        
        return Response({"error": "Invalid OTP."}, status=400)
