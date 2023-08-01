from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('goals/', views.goals_index, name='index'),
    path('goals/create/', views.GoalCreate.as_view(), name='goals_create'),
]


