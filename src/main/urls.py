from django.urls import path
from main.views import (
    FacultyListAPIView,
    GroupListAPIView,
    ScholarshipListAPIView,
    StudentListAPIView,
    StudentDetailAPIView,
    MarkListAPIView,
    SemesterListAPIView,
    AllStudentsListAPIView
)

urlpatterns = [
    path('faculties/', FacultyListAPIView.as_view(), name='faculty-list'),
    path('groups/', GroupListAPIView.as_view(), name='group-list'),
    path('scholarships/', ScholarshipListAPIView.as_view(), name='scholarship-list'),
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<str:slug>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('semesters/', SemesterListAPIView.as_view(), name='semester-list'),
    path('marks/', MarkListAPIView.as_view(), name='mark-list'),
    # Added StudentsList path
    path('students-list/', AllStudentsListAPIView.as_view(), name='students-list'),
]