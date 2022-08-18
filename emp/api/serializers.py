from rest_framework import serializers

from api.models import LeaveRequest
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='employee.first_name')
    last_name = serializers.CharField(source='employee.last_name')
    email = serializers.CharField(source='employee.email')
    class Meta:
        model = LeaveRequest
        fields = ('first_name','last_name','email','leave_name','start_date','end_date')

# class EmployeeSerializer(serializers.ModelSerializer):
#     first_name = serializers.CharField(source='employee')
#     last_name = serializers.CharField(source='employee')
#     email = serializers.CharField(source='employee')
#     class Meta:
#         model = LeaveRequest
#         fields = ('first_name','last_name','email','leave_name','start_date','end_date')

# class EmployeeSerializer(serializers.ModelSerializer):
#     # leave_name = serializers.SerializerMethodField()
#     # leave_name = serializers.StringRelatedField(many=True)
#     # start_date = serializers.DateField(source='leaverequest.start_date')
#     # end_date = serializers.DateField(source='leaverequest.end_date')

#     class Meta:
#         model = Employee
#         fields = ('first_name','last_name','email',)#'start_date','end_date')

    # def get_leave_name(self,obj):
    #     return obj.leaverequest_set.all().values_list('leave_name',flat=True)
