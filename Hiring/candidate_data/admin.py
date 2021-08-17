from django.contrib import admin
from . models import candidate_data

"""
we need to register model candidate_data here too access it from admin pannel 

"""
admin.site.register(candidate_data)