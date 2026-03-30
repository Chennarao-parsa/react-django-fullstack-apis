from rest_framework import serializers
from DBapp.models import Employee,Department
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
class CustomSerializer(serializers.Serializer):
    empno = serializers.IntegerField()
    ename = serializers.CharField(max_length=20)
    salary = serializers.IntegerField()
    bonus = serializers.IntegerField()
    dept = serializers.IntegerField()
     
    def validate(self,validated_data):
        if validated_data['salary']<0:
            raise ValidationError('Negative sal is not allowed')
        return validated_data
    def create(self,validated_data):
        #processing logic
        dobj = Department.objects.get(deptno=validated_data['dept'])
        eobj=Employee.objects.create(empno=validated_data['empno'],
                                ename=validated_data['ename'],
                                salary=validated_data['salary']+validated_data['bonus'],
                                dept=dobj
                                )
        return eobj
    def update(self,instance,validated_data):
        dobj=Department.objects.get(deptno=validated_data['dept'])
        instance.ename=validated_data['ename']
        instance.salary=validated_data['salary']+validated_data['bonus']
        instance.dept=dobj
        instance.save()
        return instance
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields =["username","password","email"]




