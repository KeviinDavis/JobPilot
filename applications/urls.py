from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/new/', views.job_create, name='job_create'),
    path('signup/', views.signup, name='signup'), 
    path('logout/', views.custom_logout, name='logout'),
]
