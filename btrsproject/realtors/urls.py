from django.urls import path
from . import views

urlpatterns = [
    path('', views.realtors, name='realtors'),
    path('<str:realtor_name>', views.realtor, name='realtor'),
]