from django import forms
from .models import Goal, Activity

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'


