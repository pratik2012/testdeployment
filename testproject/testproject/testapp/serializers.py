from rest_framework import serializers
from testproject.testapp.models import *


class EmployeeSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'