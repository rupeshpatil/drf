from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from employees.serializers import EmployeeSerializer
from employees.models import Employees
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

class Employees(APIView):


    def get(self, request):
        queryset = Employees.objects.all()
        serializer=EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)