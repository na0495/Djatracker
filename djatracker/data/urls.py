from django.urls import path
from .views import calculate_distance_view

app_name = "data"

urlpatterns = [
    path('', calculate_distance_view),
]
