from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('iindex',views.iindex,name='iindex'),
    path('save',views.save,name='save'),
    path('login/',views.login,name='login'),
    path('list_doc/',views.list_doc,name='list_doc'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
]