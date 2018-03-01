from django.urls import path
from . import views

urlpatterns = [
    path('', views.variant, name='home'),
    path('variant/', views.variant, name='variant'),
]
