2wfrom django.db import models


class Employee(models.Model):
    first_name=models.CharField(max_length=20,blank=True,null=True)
    last_name = models.CharField(max_length=20,blank=True,null=True)
    phone = models.CharField(max_length =10,blank=True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.first_name

LEAVE_STATUS_CHOICES = (
    ("APPROVED", "APPROVED"),
    ("PENDING", "PENDING"),
    ("REJECTED", "REJECTED"),
    ("CANCELLED", "CANCELLED"),
)

LEAVE_TYPE_CHOICES = (
    ("ANNUAL_LEAVE", "ANNUAL_LEAVE"),
    ("CASUAL_LEAVE", "CASUAL_LEAVE"),
    ("SICK_LEAVE", "SICK_LEAVE"),
)
# Create your models here.
class LeaveRequest(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    request_date = models.DateField(
        null=True,
        blank=True,
    )
    start_date = models.DateField(
        null=True,
        blank=True,
    )
    end_date = models.DateField(
        null=True,
        blank=True,
    )
    leave_date_details = models.JSONField(default=dict, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=LEAVE_STATUS_CHOICES,
        default="PENDING",
        null=True,
        blank=True,
    )
    reason = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    comments = models.JSONField(default=dict, blank=True, null=True)
    leave_name = models.CharField(
        max_length=100,
        choices=LEAVE_TYPE_CHOICES,
        default="CASUAL_LEAVE",
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.leave_name
