from django.db import models
# from django.urls import reverse
# from datetime import date
# User Auth Model below:
from django.contrib.auth.models import User

class FitnessCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    fitness_category = models.ForeignKey(FitnessCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Goal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    fitness_category = models.ForeignKey(FitnessCategory, on_delete=models.CASCADE)
    activities = models.CharField(max_length=200, default='default_value')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
