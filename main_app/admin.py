from django.contrib import admin
from .models import Goal, FitnessCategory

# Register your models here.
admin.site.register(Goal)
admin.site.register(FitnessCategory)

