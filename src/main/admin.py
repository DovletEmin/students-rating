from django.contrib import admin
from unfold.admin import ModelAdmin
from main import models


class BaseModelAdmin(ModelAdmin):
    list_display = ['id', 'title', 'is_active', 'formatted_created_at', 'formatted_updated_at']
    search_fields = ['title']
    list_filter = ['is_active']
    ordering = ['-id']
    
    def formatted_created_at(self, obj):
        return obj.created_at.strftime('%d.%m.%Y %H:%M')
    formatted_created_at.short_description = 'Created At'

    def formatted_updated_at(self, obj):
        return obj.updated_at.strftime('%d.%m.%Y %H:%M')
    formatted_updated_at.short_description = 'Updated At'

@admin.register(models.Faculty)
class FacultyAdmin(BaseModelAdmin):
    pass
    
    
@admin.register(models.Group)
class GroupAdmin(BaseModelAdmin):
    pass
    
    
@admin.register(models.Scholarship)
class ScholarshipAdmin(BaseModelAdmin):
    pass


@admin.register(models.Student)
class StudentAdmin(BaseModelAdmin):
    list_display = ('id', 'fullname', 'student_id',  'is_active', 'formatted_created_at', 'formatted_updated_at')
    search_fields = ('first_name', 'last_name', 'student_id')
    
    
@admin.register(models.Lesson)
class LessonAdmin(BaseModelAdmin):
    pass


@admin.register(models.Semester)
class SemesterAdmin(BaseModelAdmin):
    pass

@admin.register(models.Marks)
class MarksAdmin(BaseModelAdmin):
    list_display = ['id', 'student', 'lesson', 'semester', 'mark_type', 'mark', 'is_active']
    search_fields = ['student__first_name', 'student__last_name', 'lesson__title', 'semester__title']
    list_filter = ['is_active', 'student', 'lesson', 'semester']
    ordering = ['-id']