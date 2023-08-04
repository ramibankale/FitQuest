from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/create/', views.create_user_profile, name='create_user_profile'),
    path('profile/update/', views.update_user_profile, name='update_user_profile'),
    path('goals/', views.goals_index, name='index'),
    path('goals/create/', views.GoalCreate.as_view(), name='goals_create'),
]


