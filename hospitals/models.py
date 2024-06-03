from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  # Add additional user profile fields here (optional)

  # Add a field for user role (e.g., 'admin', 'user')
  role = models.CharField(max_length=20, choices=(('admin', 'Admin'), ('user', 'User')))

  def __str__(self):
    return self.user.username

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
       return self.name;

class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    address = models.CharField(max_length=50)

    def __str__(self):
       return self.name;

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
       return self.doctorname+"--"+self.patient.name;

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=300, null=True)
    msgdate = models.DateField(null=True)
    isread = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.id
