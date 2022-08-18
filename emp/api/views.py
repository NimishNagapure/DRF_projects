from django.http import HttpResponse
from django.shortcuts import render
from httplib2 import Response
from django.db.models import F
from django.db.models import Q
from .serializers import EmployeeSerializer
from .models import Employee, LeaveRequest
from rest_framework.views import APIView

# Create your views here.

# Fetch Leave Request for a  employee
class LeftJoin(APIView):
    def get(self, request):
        # get leaves
        leaves = LeaveRequest.objects.select_related("employee")
        print(leaves)
        for leave in leaves:
            print(leave.employee.first_name + " " + leave.leave_name)
        # emp = leaves.employee.first_name
        # print(emp)
        print(leaves.query)
        serializer = EmployeeSerializer(leaves, many=True)
        return HttpResponse(serializer.data)

    # def get(self, request):
    #     # perform full outer join in django
    #     data = LeaveRequest.objects.annotate(
    #         full_name=F("employee__first_name")
    #     ).filter(full_name__contains="Nimish")
    #     print(data.query)
    #     print(data)
    #     serializer = EmployeeSerializer(data, many=True)
    #     return HttpResponse(serializer.data)


# class LeftJoin(APIView):
#     def get(self,request):
#         # get leaves
#         employee = Employee.objects.prefetch_related('leaverequest_set')
#         print(employee.query)
#         serializer = EmployeeSerializer(employee,many=True)
#         return HttpResponse(serializer.data)


class InnerJoin(APIView):
    def get(self, request):
        # get leaves
        leaves = LeaveRequest.objects.filter(employee__first_name="Nimish")
        print(leaves)
        print(leaves.query)
        serializer = EmployeeSerializer(leaves, many=True)
        return Response(serializer.data)

    def _get(self, request):
        # perform full outer join in django
        data = LeaveRequest.objects.filter(leave_name="CASUAL_LEAVE").select_related(
            "employee"
        )
        print(data.query)
        print(data)
        serializer = EmployeeSerializer(data, many=True)
        return HttpResponse(serializer.data)

    def get(self, request):
        data = (
            LeaveRequest.objects.filter(employee_id=1)
            .annotate(full_name=F("employee__first_name"))
            .filter(leave_name__contains="CASUAL_LEAVE")
        )
        print(data.query)
        print(data)
        serializer = EmployeeSerializer(data, many=True)
        return HttpResponse(serializer.data)

    def get(self, request):
        # perform right outer join in django
        leave_request = LeaveRequest.objects.select_related("employee").filter(
            employee__isnull=False
        )
        print(leave_request.query)
        print(leave_request)
        serializer = EmployeeSerializer(leave_request, many=True)
        return HttpResponse(serializer.data)


class _InnerJoin(APIView):
    def get(self, request):
        employee = (
            Employee.objects.all()
            .prefetch_related("leaverequest_set")
            .filter(leaverequest__status="PENDING")
        )
        print(employee.query)
        print(employee)
        return HttpResponse(employee)


class FullOuterJoin(APIView):
    def get(self, request):
        # perform full outer join in django
        data = LeaveRequest.objects.annotate(
            full_name=F("employee__first_name")
        ).filter(full_name__contains="Nimish")
        print(data.query)
        print(data)
        serializer = EmployeeSerializer(data, many=True)
        return HttpResponse(serializer.data)


from django.db.models import Count


class RightJoin(APIView):
    def get(self, request):
        # perform right outer join in django

        # leave_request= Employee.objects.filter(id=1).annotate(
        #     count=Count("leaverequest")
        # )
        leave_request = Employee.objects.get(id=1).leaverequest_set.all()
        print(leave_request.query)
        print(leave_request)
        serializer = EmployeeSerializer(leave_request, many=True)
        return HttpResponse(serializer.data)
