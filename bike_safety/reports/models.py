from django.db import models

class ViolationReport(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    license_plate = models.CharField(max_length=20)
    distance = models.FloatField()
    speed = models.IntegerField()
    gps = models.CharField(max_length=255)
    observations = models.TextField()
    photo = models.ImageField(upload_to='violation_photos/', null=True, blank=True)  # Optional for photo of number plate

    def __str__(self):
        return f"Report {self.id} - {self.license_plate}"
