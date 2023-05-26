from django.urls import path
from .views import CancerPrediction

urlpatterns = [
    path('result/', CancerPrediction.as_view(), name = 'weight_prediction'),
]