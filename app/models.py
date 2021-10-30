from django.db import models

# All models are new!
class Days(models.Model):
    day = models.TextField(max_length=255, blank=True, null=True)
    
class Time(models.Model):
    From = models.TextField(max_length=255, blank=True, null=True)
    To = models.TextField(max_length=255, blank=True, null=True)
    
class Doctors(models.Model):
    doctor_name = models.CharField(max_length=255)
    