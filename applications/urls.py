from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/new/', views.job_create, name='job_create'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/<int:job_id>/edit/', views.job_update, name='job_update'),
    path('jobs/<int:job_id>/delete/', views.job_delete, name='job_delete'),
    path('signup/', views.signup, name='signup'), 
    path('logout/', views.custom_logout, name='logout'),
]
