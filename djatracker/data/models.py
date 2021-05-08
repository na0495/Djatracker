from django.db import models
from django.utils import timezone

# Create your models here.


class store (models.Model):
    TRAVEL_CHOICES = (
        ("Driving", "Driving"),
        ("Transit", "Transit"),
        ("Walking", "Walking"),
        ("Cycling", "Cycling"),
        ("Flights", "Flights"),
    )
    starting_point = models.CharField(max_length=150, blank=True, null=True)
    destination_point = models.CharField(max_length=150, blank=True, null=True)
    distance = models.DecimalField(
        max_length=50, max_digits=10, decimal_places=3, blank=True, null=True)
    travel_time = models.DateField(blank=True, null=True)
    starting_time = models.DateField(blank=True, null=True)
    arrival_time = models.DateField(blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    travel_mode = models.CharField(max_length=30, choices=TRAVEL_CHOICES)

    def __str__(self):
        return f"Travling from {self.starting_point} to {self.destination_point} with the approximity distance of {self.distance} km"
