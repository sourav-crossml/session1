import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    """
    this function will validate that input file should be pdf only
    """
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def file_size(value):
    """
    this function will validate file size is less then 5mb
    """
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')