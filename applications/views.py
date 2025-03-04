from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import JobApplication
from .forms import JobApplicationForm 

@login_required
def job_list(request):
    jobs = JobApplication.objects.filter(user=request.user)  
    return render(request, 'applications/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id, user=request.user)
    return render(request, 'applications/job_detail.html', {'job': job})

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user 
            job.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'applications/job_form.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('job_list') 
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def custom_logout(request):
    logout(request)
    return redirect('login')
