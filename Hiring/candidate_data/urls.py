from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.save_data, name='index'),
    path('details/', views.show_details, name='details'),
    path('candidate/<int:id>/', views.show_individual_data, name="candidate"),
    
]