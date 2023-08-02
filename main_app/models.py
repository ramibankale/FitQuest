from django.db import models

# User Auth Model below:
from django.contrib.auth.models import User

# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=255)
    # One user --< has many goals therefore goals has FK 
    # user authen linking a goal to a user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    