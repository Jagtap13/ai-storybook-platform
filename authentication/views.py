from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = None
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        profile = user.studentprofile
        return Response({
            'username': user.username,
            'email': user.email,
            'role': profile.role,
            'age': profile.age,
        })
