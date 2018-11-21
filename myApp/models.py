import django_filters
from django.db import models
from django.forms import ModelForm
from shoppls import settings

GENDER_CHOISES = (
    ('Mужской', 'Мужской'), ('Женский', 'Женский'),
)
# ==========================================================
from django.contrib.auth.models import User
from django import forms

class UserProfileInfo(models.Model):
    is_doctor = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=80, default='Не указано')
    surname = models.CharField(max_length=80, default='Не указано')
    patronymic = models.CharField(max_length=80, default='Не указано')

    # portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
# ==========================================================

class Wing(models.Model):
    name = models.CharField(max_length=80, default='Не указано')
    color = models.CharField(max_length=30, default='Не указано')

    def __str__(self):
        return self.name


class Patient(models.Model):
    # braclet id
    z_id = models.CharField(max_length=16, default='0')

    # dispay params
    name = models.CharField(max_length=80, default='Не указано')
    surname = models.CharField(max_length=80, default='Не указано')
    patronymic = models.CharField(max_length=80, default='Не указано')
    room = models.CharField(max_length=30, default='Не указано')

    # non-display params
    age = models.DateField(null=True)
    cause = models.CharField(max_length=300, default='Не указано')
    gender = models.CharField(max_length=30, default='Не указано', choices=GENDER_CHOISES)
    wing = models.ForeignKey(Wing, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class PatientList(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    time_of_call = models.DateTimeField(null=True)

    def __str__(self):
        return self.patient.name


class PatientLog(models.Model):
    patient =  models.ForeignKey(Patient, on_delete=models.CASCADE)
    time_of_call = models.DateTimeField(null=True)
    time_of_answer = models.DateTimeField(null=True)
    worker =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name
# class UserFilter(django_filters.FilterSet):


