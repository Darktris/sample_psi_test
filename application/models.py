from django.db import models

# Create your models here.
class Patient(models.Model):
    nameP = models.CharField(max_length=256)

    def __str__(self):
        return self.nameP

class Doctor(models.Model):
    nameD = models.CharField(max_length=256)

    def __str__(self):
        return self.nameD

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return self.doctor.nameD + ' ' + self.patient.nameP
