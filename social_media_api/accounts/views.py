from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def retrieve(self, request, *args, **kwargs):
        # Fetch user profile by ID
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

