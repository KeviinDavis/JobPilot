from django.contrib import admin
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'status', 'date_applied', 'user')
    list_filter = ('status', 'company_name')
    search_fields = ('job_title', 'company_name', 'user__username')

# Register models below:
