from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.fields import flatten_choices_dict
from .models import UserProfile
from rest_framework import permissions, serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserProfileSerializers,UserSerializer


class registerView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request):
        data = request.user
        user = User.objects.create(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


# I need to know how jwt is working to be able make the user request and also login request possible