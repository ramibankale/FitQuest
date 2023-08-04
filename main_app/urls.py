from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),  # Update 'index' URL pattern
    path('about/', views.about, name='about'),
    path('goals/', views.GoalList.as_view(), name='goals_index'),
    path('goals/create/', views.GoalCreate.as_view(), name='goal_create'),
    path('goals/<int:pk>/', views.GoalDetail.as_view(), name='goal_detail'),
    path('goals/<int:pk>/update/', views.GoalUpdate.as_view(), name='goal_update'),
    path('goals/<int:pk>/delete/', views.GoalDelete.as_view(), name='goal_delete'),
    path('goals/<int:pk>/save/', views.save_goal, name='goal_save'),

    path('goals/<int:goal_id>/assoc_activity/<int:activity_id>/', views.assoc_activity, name='assoc_activity'),
    path('goals/<int:goal_id>/unassoc_activity/<int:activity_id>/', views.unassoc_activity, name='unassoc_activity'),
    path('activities/', views.ActivityList.as_view(), name='activity_list'),
    path('activity/<int:pk>/', views.ActivityDetail.as_view(), name='activity_detail'),
    path('activity/create/', views.ActivityCreate.as_view(), name='activity_create'),
    path('activity/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activity_update'),
    path('activity/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activity_delete'),
]
