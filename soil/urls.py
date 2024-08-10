# soil_analysis/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_soil_test, name='input_soil_test'),
    path('recommendation/<int:test_id>/', views.view_recommendation, name='view_recommendation'),
]
