from django.shortcuts import render

# Create your views here.
from testproject.testapp.models import *
from testproject.testapp.serializers import *
from rest_framework import generics


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialiser
