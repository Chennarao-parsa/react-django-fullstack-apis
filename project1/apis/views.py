from rest_framework.views import APIView
from rest_framework.response import Response
from DBapp.models import Employee
from django.http import JsonResponse
from .serializers import EmpSerializer,CustomSerializer,UserSerializer
from rest_framework.status import HTTP_201_CREATED,\
HTTP_400_BAD_REQUEST,HTTP_200_OK
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ViewSet
import json
class GetEmpAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request):
        emps = Employee.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size=3
        pages=paginator.paginate_queryset(emps,request)
        s_obj = EmpSerializer(pages, many=True)
        return paginator.get_paginated_response(s_obj.data)
    def post(self,request):
        s_obj= EmpSerializer(data = request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return  Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
class ModifyEmpAPI(APIView):
    def getemployee(self,pk):
        emp = Employee.objects.get(empno=pk)
        return emp
    def get(self,request,pk):
        emp = self.getemployee(pk)
        s_obj = EmpSerializer(emp)
        return Response(s_obj.data)
    def put(self,request,pk):
        emp = self.getemployee(pk)
        s_obj=EmpSerializer(emp,data=request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        emp = self.getemployee(pk)
        emp.delete()
        return Response(status=HTTP_200_OK)
class CustomInsertAPI(APIView):
    def get(self,request):
        emps=Employee.objects.all()
        s_obj=EmpSerializer(emps,many=True)
        return Response(s_obj.data)

    def post(self,request):
        s_obj=CustomSerializer(data=request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
def sendsms(obj):
    print(f"sending a message to {obj.validated_data['ename']}")
class CustomModifyAPI(APIView):
    def get(self,request,pk):
        emp=Employee.objects.get(empno=pk)
        s_obj=EmpSerializer(emp)
        return Response(s_obj.data,status=HTTP_200_OK)
    def put(self,request,pk):
        emp = Employee.objects.get(empno=pk)
        s_obj=CustomSerializer(emp,data=request.data)
        if s_obj.is_valid()== True:
            sendsms(s_obj)
            s_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
class RegisterUserAPI(APIView):
    def post(self,request):
        s_obj=UserSerializer(data=request.data)
        if s_obj.is_valid() == True:
            u_obj=s_obj.save()
            u_obj.set_password(s_obj.validated_data['password'])
            u_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
class SearchAPIView(APIView):
    def get(self,request):
        search=request.query_params.get('search')
        emps=Employee.objects.filter(ename__icontains=search)
        s_obj=EmpSerializer(emps,many=True)
        return Response(s_obj.data)
class EmpGenericAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmpSerializer
    filter_backends=[SearchFilter]
    search_fieds=['ename', 'salary']
class EmpViewSet(ViewSet):
    def list(self,request):
        emps=Employee.objects.all()
        s_obj=EmpSerializer(emps,many=True)
        return Response(s_obj.data)
    def create(self,request):
        s_obj=EmpSerializer(data=request.data)
        if s_obj.is_valid()==True:
            s_obj.save()
            return Response(s_obj.data,HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        emp =Employee.objects.get(empno=pk)
        s_obj=EmpSerializer(emp)
        return Response(s_obj.data)
    def update(self,request,pk):
        emp = Employee.objects.get(empno=pk)
        s_obj=EmpSerializer(emp,data=request.data)
        if s_obj.is_valid()==True:
            return Response(status=HTTP_200_OK)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        emp=Employee.objects.get(empno=pk)
        emp.delete()
        return Response(status=HTTP_200_OK)
