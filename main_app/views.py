from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Goal
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

goals = [
  {'name'},
]

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def user_profile(request):
  user_profile = UserProfile.objects.get(user=request.user)
  return render(request, 'user_profile.html', {'user_profile': user_profile})

@login_required
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm()
    return render(request, 'create_user_profile.html', {'form': form})

@login_required
def update_user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'update_user_profile.html', {'form': form})

def goals_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'goals/index.html', {
    'goals': goals
  })

class GoalCreate(CreateView):
  model = Goal
  fields = '__all__'