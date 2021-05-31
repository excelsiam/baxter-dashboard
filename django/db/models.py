from django.db import models


class BasicInformation(models.Model):
    name = models.CharField(null=True, max_length=50)
    code_id = models.CharField(null=True, max_length=50)
    hospital = models.CharField(null=True, max_length=30)
    gender = models.CharField(null=True, max_length=10)
    birth_date = models.DateField(null=True)
    education = models.CharField(null=True, max_length=20)
    payment = models.IntegerField(null=True)
    primary_kidney_disease = models.CharField(null=True, max_length=10)
    dm_status = models.BooleanField(null=True, default=False)
    pd_initiation_date = models.DateField(null=True)
    dropout_date = models.DateField(null=True)
    dropout_category = models.CharField(null=True, max_length=50)
    dropout_cause = models.CharField(null=True, max_length=150)
    remarks = models.TextField(null=True)


class PDInfection(models.Model):
    name = models.CharField(null=True, max_length=50)
    date = models.DateField(null=True)
    type_of_infection = models.CharField(null=True, max_length=50)
    causative_organism = models.CharField(null=True, max_length=150)
    outcomes = models.CharField(null=True, max_length=255)
    remarks = models.TextField(null=True)


class Hospitalization(models.Model):
    name = models.CharField(null=True, max_length=50)
    admission_date = models.DateField(null=True)
    reason = models.CharField(null=True, max_length=255)
    remarks = models.TextField(null=True)
