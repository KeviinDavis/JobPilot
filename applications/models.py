from django.db import models
from django.contrib.auth.models import User  

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interviewing', 'Interviewing'),
        ('Offer Received', 'Offer Received'),
        ('Rejected', 'Rejected'),
        ('Accepted', 'Accepted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    date_applied = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    notes = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.status})"
