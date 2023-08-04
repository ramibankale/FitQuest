from django.db import models

# User Auth Model below:
from django.contrib.auth.models import User

# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=255)
    # One user --< has many goals therefore goals has FK 
    # user authen linking a goal to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    weight = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return f"{self.user.username}'s Profile"
    