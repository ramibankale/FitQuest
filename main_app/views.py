from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django import forms
from .models import Goal, Activity, FitnessCategory  

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def goals_index(request):
    goals = Goal.objects.all()
    return render(request, 'goals/index.html', {
        'goals': goals
    })

class GoalForm(forms.ModelForm):
    fitness_category = forms.ModelChoiceField(queryset=FitnessCategory.objects.all(), widget=forms.Select)

    class Meta:
        model = Goal
        fields = '__all__'

class GoalCreate(CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/goal_form.html'

    def get_success_url(self):
        return '/goals/'  

class GoalUpdate(UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/goal_form.html'

    def get_success_url(self):
        return '/goals/'  # Redirect to the goals index page after updating a goal

class GoalDelete(DeleteView):
    model = Goal
    success_url = '/goals/'  # Redirect to the goals index page after deleting a goal

def save_goal(request, pk):
    if request.method == 'POST':
        goal = Goal.objects.get(pk=pk)
        activities = request.POST.get('activities', '')
        goal.activities = activities
        goal.save()
    return redirect('goal_detail', pk=pk)

class GoalDetail(DetailView):
    model = Goal
    template_name = 'goals/goal_detail.html'  # Replace this with your desired template path for goal detail
    context_object_name = 'goal'

class GoalList(ListView):
    model = Goal
    template_name = 'goals/index.html'
    context_object_name = 'goals'

class ActivityList(ListView):
  model = Activity

class ActivityDetail(DetailView):
  model = Activity

class ActivityCreate(CreateView):
  model = Activity
  fields = '__all__'

class ActivityUpdate(UpdateView):
  model = Activity
  fields = ['name']

class ActivityDelete(DeleteView):
  model = Activity
  success_url = '/activity'

def assoc_activity(request, goal_id, activity_id):
    goal = Goal.objects.get(id=goal_id)
    activity = Activity.objects.get(id=activity_id)
    goal.activities.add(activity)
    return redirect('goal_detail', pk=goal_id)

def unassoc_activity(request, goal_id, activity_id):
    goal = Goal.objects.get(id=goal_id)
    activity = Activity.objects.get(id=activity_id)
    goal.activities.remove(activity)
    return redirect('goal_detail', pk=goal_id)