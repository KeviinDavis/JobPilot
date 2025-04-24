from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import JobApplication
from .forms import JobApplicationForm 
from django.contrib import messages

def home(request):
    return render(request, 'applications/home.html')

@login_required
def job_list(request):
    jobs = JobApplication.objects.filter(user=request.user)  
    status_categories = ["Applied", "Interviewing", "Offer Received", "Rejected", "Accepted"]  # Pass this to the template
    return render(request, 'applications/job_list.html', {'jobs': jobs, 'status_categories': status_categories})


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

@login_required
def job_update(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'applications/job_form.html', {'form': form})

    
@login_required
def job_delete(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id, user=request.user)
    job.delete()
    messages.success(request, "Job application deleted successfully.")
    return redirect('job_list')

@login_required
def update_status(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id, user=request.user)
    
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(JobApplication.STATUS_CHOICES):
            job.status = new_status
            job.save()
            messages.success(request, f"Status updated to {new_status}!")
    
    return redirect("job_list")


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
