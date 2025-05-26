from rest_framework import serializers
from main import models

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = (
            'id',
            'title',
            'slug',
        )
        

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = (
            'id',
            'title',
            'slug',
        )
        
        
class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Scholarship
        fields = (
            'id',
            'title',
            'slug',
        )
        
        
class StudentSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)
    group = GroupSerializer(read_only=True)
    scholarship = ScholarshipSerializer(read_only=True)
    
    class Meta:
        model = models.Student
        fields = (
            'id',
            'fullname',
            'student_id',
            'profile_picture',
            'slug',
            'faculty',
            'group',
            'scholarship',
        )   
        
        
        
class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Semester
        fields = (
            'id',
            'title',
            'slug',
        )
        
        
class MarkSerializer(serializers.ModelSerializer):
    lesson = serializers.CharField(source='lesson.title')
    semester = serializers.CharField(source='semester.title')
    
    class Meta:
        model = models.Marks
        fields = (
            'id',
            'lesson',
            'semester',
            'mark_type',
            'mark',
        )    