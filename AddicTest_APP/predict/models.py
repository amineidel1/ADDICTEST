from django.db import models
from django.contrib import admin

# Create your models here.


class User_experience(models.Model):
    Age = models.CharField(max_length=200)
    Gender = models.CharField(max_length=200)
    Eduction = models.CharField(max_length=200)
    Contry = models.CharField(max_length=200)
    Ethnicity = models.CharField(max_length=200)
    Nscore = models.DecimalField(max_digits=7, decimal_places=5)
    Escore = models.DecimalField(max_digits=7, decimal_places=5)
    Oscore = models.DecimalField(max_digits=7, decimal_places=5)
    Ascore = models.DecimalField(max_digits=7, decimal_places=5)
    Cscore = models.DecimalField(max_digits=7, decimal_places=5)
    Impulsive = models.DecimalField(max_digits=7, decimal_places=5)
    SS = models.DecimalField(max_digits=7, decimal_places=5)

    proba_Alcohol = models.DecimalField(max_digits=5, decimal_places=2)
    proba_Amphet = models.DecimalField(max_digits=5, decimal_places=2)
    proba_Coke = models.DecimalField(max_digits=5, decimal_places=2)
    proba_Cannabis = models.DecimalField(max_digits=5, decimal_places=2)
    proba_Ecstasy = models.DecimalField(max_digits=5, decimal_places=2)
    proba_Legalh = models.DecimalField(max_digits=5, decimal_places=2)
    proba_LSD = models.DecimalField(max_digits=5, decimal_places=2)
    proba_Mushrooms = models.DecimalField(max_digits=5, decimal_places=2)
    proba_Nicotine = models.DecimalField(max_digits=5, decimal_places=2)
