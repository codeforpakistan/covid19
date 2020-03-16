from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Province(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name

class Laboratory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class User(AbstractUser):
    laboratory = models.ForeignKey(Laboratory, null=True, on_delete=models.SET_NULL)


class Hospital(models.Model):
    name = models.CharField(unique=True, max_length=100)
    province = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100, null=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    age = models.IntegerField(null=True)
    cnic = models.CharField(max_length=13, null=True)
    phone = models.CharField(max_length=15, null=True)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    province = models.ForeignKey(Province, null=True, on_delete=models.SET_NULL)
    hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    source = models.ForeignKey(Source, null=True, on_delete=models.SET_NULL)
    confirmation_date = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
