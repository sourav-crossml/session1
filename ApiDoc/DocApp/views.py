from DocApp.serializers import DocumentSerializer
from DocApp.models import Document
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

users = User.objects.all()
"""
this loop will generate token for new users 
"""

for user in users:
    token, created = Token.objects.get_or_create(user=user)
    print (user.username, token.key)

class DocumentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Document instances.
    """
    permission_classes = (IsAuthenticated,) 
    authentication_classes = (TokenAuthentication,) 

    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    