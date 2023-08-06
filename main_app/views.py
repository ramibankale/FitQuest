from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django import forms
from .models import Goal, Activity, FitnessCategory  
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required 
def goals_index(request):
    goals = Goal.objects.all()
    return render(request, 'goals/index.html', {
        'goals': goals
    })

class GoalForm(LoginRequiredMixin, forms.ModelForm):
    fitness_category = forms.ModelChoiceField(queryset=FitnessCategory.objects.all(), widget=forms.Select)

    class Meta:
        model = Goal
        fields = '__all__'

class GoalCreate(LoginRequiredMixin, CreateView):
    model = Goal
    # form_class = GoalForm'
    fields =['name', 'description', 'fitness_category', 'activities', 'start_date', 'end_date']
    template_name = 'main_app/goal_form.html'

    def form_valid(self, form):
        # self.request.user is the logged in user
        form.instance.user = self.request.user
        # Let the CreateView's form_valid method
        # do its regular work (saving the object & redirecting)
        return super().form_valid(form)

    def get_success_url(self):
        return '/goals'  

class GoalUpdate(LoginRequiredMixin, UpdateView):
    model = Goal
    fields = '__all__'
    template_name = 'main_app/goal_form.html'

    def get_success_url(self):
        return '/goals'  # Redirect to the goals index page after updating a goal

class GoalDelete(LoginRequiredMixin, DeleteView):
    model = Goal
    # template_name = 'goals/index.html'
    success_url = '/goals'  # Redirect to the goals index page after deleting a goal

    def get_success_url(self):
        return '/goals'  # Redirect to the goals index page after updating a goal


@login_required 
def save_goal(request, pk):
    if request.method == 'POST':
        goal = Goal.objects.get(pk=pk)
        activities = request.POST.get('activities', '')
        goal.activities = activities
        goal.save()
    return redirect('goal_detail', pk=pk)

class GoalDetail(LoginRequiredMixin, DetailView):
    model = Goal
    template_name = 'goals/goal_detail.html'  # Replace this with your desired template path for goal detail
    # context_object_name = 'goal'

class GoalList(LoginRequiredMixin, ListView):
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

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(name, email, password)
        user.save()

        return redirect('home')

    else:
        return render(request, 'signup.html')


# def user_profile(request, user_id):
#     user = User.objects.get(id=user_id)
#     context = {
#         'user': user,
#     }
#     return render(request, 'user_profile.html', context)

# def create_user_profile(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             return redirect('profile')
#     else:
#         form = UserCreationForm()
#     return render(request, 'create_user_profile.html', {'form': form})