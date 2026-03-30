from django.urls import path
from .import views 
urlpatterns=[
    path('add/',views.add_student,name='add_student'),
    path('list/',views.list_students,name='list_students'),
    path('delete/<int:id>/',views.delete_student,name='delete_student'),
    path('update/<int:id>/',views.update_student,name='update_student'),
]