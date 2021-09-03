from django.urls import path,include
from .views import DocumentViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'document', DocumentViewSet, basename='document')
urlpatterns =[
    path('', include(router.urls)),
]