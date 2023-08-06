from django.db import models
# from django.urls import reverse
# from datetime import date
# User Auth Model below:
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    activities = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
# hooking the create_user_profile and save_user_profile methods to the UserProfile model whenever a save event occurs    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
