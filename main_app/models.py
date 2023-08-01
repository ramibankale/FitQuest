from django.db import models

# Create your models here.
class Goal(models.Model):
    title = models.CharField(max_length=255)
    