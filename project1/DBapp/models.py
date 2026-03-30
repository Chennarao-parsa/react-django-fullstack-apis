from django.db import models



class Department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=20)
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.dname

class Employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    salary=models.IntegerField(null=True)
    dept=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    profile_pic=models.ImageField(upload_to='images/',null=True)
    video=models.FileField(upload_to='videos/',null=True)
    def __str__(self):
        return self.ename
# Create your models here.
