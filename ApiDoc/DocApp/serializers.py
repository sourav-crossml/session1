from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    """
    this class will serialize document model
    """
    class Meta:
        model = Document
        fields='__all__'