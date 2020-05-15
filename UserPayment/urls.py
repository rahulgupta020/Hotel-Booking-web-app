from django.urls import path, include
from .import views	

urlpatterns=[
    path('userpayment/', views.userpayment, name='userpayment'),
]