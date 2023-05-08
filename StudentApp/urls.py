

from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_api, name='students'),
    path('students/<int:id>/', views.student_api, name='student-detail'),
]