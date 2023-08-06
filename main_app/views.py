from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django import forms
from .models import Goal, Activity, FitnessCategory  
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm



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
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def user_profile(request):
    # Get the user's profile associated with the logged-in user
    profile = request.user.profile

    return render(request, 'profile/user_profile.html', {'user': request.user, 'profile': profile})

@login_required
def update_user_profile(request, user_id):
    # Retrieve the correct Profile instance based on the user_id
    profile = get_object_or_404(Profile, user_id=user_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # Redirect to the user profile page after successful update
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/update_user_profile.html', {'form': form})
