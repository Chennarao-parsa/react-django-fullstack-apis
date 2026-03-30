from django.contrib import admin
from .models import Department, Employee
class MyAdmin(admin.ModelAdmin):
    list_display=("empno","ename","salary","grade","department")
    list_editable=["ename"]
    list_filter=["salary"]
    def grade(self,obj):
        if obj.salary>200000:
            return 'High'
        elif obj.salary>150000:
            return 'medium'
        else:
            return 'low'
    def department(self,obj):
        return obj.dept.dname if obj.dept else "No Department"
    department.short_description = "Department"
admin.site.register(Employee,MyAdmin)
admin.site.register(Department)

