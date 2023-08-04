<<<<<<< HEAD
from django import forms
from .models import Goal, Activity

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = '__all__'


=======
# forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'age', 'gender', 'weight', 'height']
>>>>>>> a4da8e21778eafa0b35755153503040919dd0e15
