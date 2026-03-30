from django.urls import path
from . import views
urlpatterns = [
    path('display/',views.dbprocessing),
    path('insert/',views.insertemployee,name='inserturl'),
    path('select/',views.selectemployee ,name='selecturl'),
    path('update/<int:empno>/',views.updateemployee,name='updateurl'),
    path('delete/<int:empno>/',views.deleteemployee,name='deleteurl'),
    ]