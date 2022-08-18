from django.contrib import admin

from api.models import LeaveRequest,Employee

# Register your models here.

admin.site.register(Employee)
admin.site.register(LeaveRequest)
