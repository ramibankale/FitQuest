from django import forms
from .models import Goal, Profile

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age', 'gender', 'weight', 'height']
