from employees.models import Employees

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['emp_no', 'birth_date', 'first_name', 'last_name','gender']