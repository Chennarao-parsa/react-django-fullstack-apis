from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.routers import DefaultRouter
from . import views
routes = DefaultRouter()
routes.register('employee',views.EmpViewSet,basename='employee')

urlpatterns=[
    path('getemployeesapi/',views.GetEmpAPI.as_view()),
    path('modifyemployeesapi/<int:pk>/',views.ModifyEmpAPI.as_view()),
    path('custominsertapi/',views.CustomInsertAPI.as_view()),
    path('custommodifyapi/<int:pk>/',views.CustomModifyAPI.as_view()),
    path('registeruserapi/',views.RegisterUserAPI.as_view()),
    path('loginapi/',TokenObtainPairView.as_view()),
    path('refreshapi/',TokenRefreshView.as_view()),
    path('searchapi/',views.SearchAPIView.as_view()),
    path('getgenericapi/',views.EmpGenericAPIView.as_view()),
    path('',include(routes.urls))
]
