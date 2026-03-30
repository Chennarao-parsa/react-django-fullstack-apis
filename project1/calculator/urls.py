from django.urls import path
from . import views

urlpatterns=[
    path('addition/',views.addition),
    path('',views.calculator),
    path('mtable/',views.generatetable),
]
