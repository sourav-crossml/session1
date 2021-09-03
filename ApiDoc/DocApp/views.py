from .models import Document
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import DocumentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes,authentication_classes,action
from rest_framework.parsers import MultiPartParser, FormParser
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
    authentication_classes=([TokenAuthentication,])
    permission_classes=([IsAuthenticated,])
    serializer_class = DocumentSerializer
    def get_queryset(self, *args, **kwargs):
        return Document.objects.filter(user=self.request.user)
