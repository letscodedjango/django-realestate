from django.urls import path
from . import views

urlpatterns = [
    path('realtors', views.realtors, name='realtors'),
    path('<str:realtor_name>', views.realtor, name='realtor'),
]