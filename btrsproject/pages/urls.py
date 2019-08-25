from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_template, name='about'),
    path('home/', views.index_template, name='home'),
]