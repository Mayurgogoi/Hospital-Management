from django.db import models
from django.utils.timezone import now


# Create your models here.
class SignupDoctor(models.Model):
    profilePic = models.ImageField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    specialist = models.CharField(max_length=150, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=6)
    password = models.JSONField(max_length=300) # JSONField because it will be stored in encripted form
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.username

class CreateBlog(models.Model):
    username = models.CharField(max_length=30)
    Title = models.CharField(max_length=200)
    Image = models.ImageField()
    Categories = models.CharField(max_length=50)
    Summary = models.TextField()
    Content = models.TextField()
    Draft = models.CharField(max_length=5, null=True)
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.username


class SignupPatient(models.Model):
    profilePic = models.ImageField()
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    password = models.JSONField(max_length=300) # JSONField because it will be stored in encripted form
    pincode = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=now)

    def __str__(self):
        return self.username

class Appointment(models.Model):
    patientUsername = models.CharField(max_length=30)
    nameOfPatient = models.CharField(max_length=80)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    def __str__(self):
        return self.patientUsername