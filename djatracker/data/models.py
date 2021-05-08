from django.contrib.gis.db import models

# Create your models here.


class MappingData (models.Model):
    destination_point = models.CharField(max_length=150, blank=True, null=True)
    starting_point = models.CharField(max_length=150, blank=True, null=True)
    destination_location_point = models.PointField()
    starting_location_point = models.PointField()
    TRAVEL_CHOICES = (
        ("Driving", "Driving"),
        ("Transit", "Transit"),
        ("Walking", "Walking"),
        ("Cycling", "Cycling"),
        ("Flights", "Flights"),
    )
    distance = models.DecimalField(
        max_length=50, max_digits=10, decimal_places=3, blank=True, null=True)
    travel_time = models.DateField(blank=True, null=True)
    starting_time = models.DateField(blank=True, null=True)
    arrival_time = models.DateField(blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    travel_mode = models.CharField(max_length=30, choices=TRAVEL_CHOICES)

    def __str__(self):
        return '%s %s' % (self.destination_point, self.starting_point)
