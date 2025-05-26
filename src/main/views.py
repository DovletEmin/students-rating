from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from main import serializers, models, pagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class FacultyListAPIView(APIView):
    @swagger_auto_schema(
        tags=['students'],
    )
    def get(self, request):
        faculties = models.Faculty.objects.filter(is_active=True)
        serializer = serializers.FacultySerializer(faculties, many=True)
        return Response(
            {
                'count': len(serializer.data),
                'results': serializer.data   
            },
            status=status.HTTP_200_OK
        )
    
    
class GroupListAPIView(APIView):
    @swagger_auto_schema(
        tags=['students']
    )
    def get(self, request):
        groups = models.Group.objects.filter(is_active=True)
        serializer = serializers.GroupSerializer(groups, many=True)
        return Response(
            {
                'count': len(serializer.data),
                'results': serializer.data   
            },
            status=status.HTTP_200_OK
        )
    
    
class ScholarshipListAPIView(APIView):
    @swagger_auto_schema(
        tags=['students']
    )
    def get(self, request):
        scholarships = models.Scholarship.objects.filter(is_active=True)
        serializer = serializers.ScholarshipSerializer(scholarships, many=True)
        return Response(
            {
                'count': len(serializer.data),
                'results': serializer.data   
            },
            status=status.HTTP_200_OK
        )
    
    
class StudentListAPIView(APIView):
    pagination_class = pagination.StandardPagination

    @swagger_auto_schema(
        tags=['students'],
        operation_description="List students with optional filtering",
        manual_parameters=[
            openapi.Parameter(
                'faculty',
                openapi.IN_QUERY,
                description="faculty slug",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'group',
                openapi.IN_QUERY,
                description="group slug",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'scholarship',
                openapi.IN_QUERY,
                description="scholarship slug",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request):
        faculty_slug = self.request.query_params.get('faculty', None)
        group_slug = self.request.query_params.get('group', None)
        scholarship_slug = self.request.query_params.get('scholarship', None)
        students = models.Student.objects.filter(is_active=True)
        if faculty_slug:
            students = students.filter(faculty__slug=faculty_slug)
        if group_slug:
            students = students.filter(group__slug=group_slug)
        if scholarship_slug:
            students = students.filter(scholarship__slug=scholarship_slug)
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(students, request)
        serializer = serializers.StudentSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    
    
class StudentDetailAPIView(APIView):
    @swagger_auto_schema(
        tags=['students'],
    )
    def get(self, request, slug):
        try:
            student = models.Student.objects.get(slug=slug, is_active=True)
            serializer = serializers.StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except models.Student.DoesNotExist:
            return Response({'detail': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    
# Added StudendsList

class AllStudentsListAPIView(APIView):
    @swagger_auto_schema(
        tags=['students'],
        operation_description="List students with optional filtering",
        manual_parameters=[
            openapi.Parameter(
                'faculty',
                openapi.IN_QUERY,
                description="faculty slug",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'group',
                openapi.IN_QUERY,
                description="group slug",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'scholarship',
                openapi.IN_QUERY,
                description="scholarship slug",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request):
        students = models.Student.objects.filter(is_active=True)
        serializer = serializers.StudentSerializer(students, many=True)
        return Response(
            {
                'count': len(serializer.data),
                'results': serializer.data   
            },
            status=status.HTTP_200_OK
        )

class SemesterListAPIView(APIView):
    @swagger_auto_schema(
        tags=['mark']
    )
    def get(self, request):
        semesters = models.Semester.objects.filter(is_active=True)
        serializer = serializers.SemesterSerializer(semesters, many=True)
        return Response(
            {
                'count': len(serializer.data),
                'results': serializer.data   
            },
            status=status.HTTP_200_OK
        )
        
        
        
class MarkListAPIView(APIView):
    @swagger_auto_schema(
        tags=['mark'],
        operation_description="List marks with optional filtering",
        manual_parameters=[
            openapi.Parameter(
                'student',
                openapi.IN_QUERY,
                description="student slug",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                'semester',
                openapi.IN_QUERY,
                description="semester slug",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request):
        student_slug = self.request.query_params.get('student', None)
        semester_slug = self.request.query_params.get('semester', None)
        marks = models.Marks.objects.filter(is_active=True)
        if student_slug:
            marks = marks.filter(student__slug=student_slug)
        if semester_slug:
            marks = marks.filter(semester__slug=semester_slug)
        serializer = serializers.MarkSerializer(marks, many=True)
        return Response(
            {
                'count': len(serializer.data),
                'results': serializer.data   
            },
            status=status.HTTP_200_OK
        )