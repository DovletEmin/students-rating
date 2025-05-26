from django.db import models
from django.utils.text import slugify
import uuid

class BaseModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        super().save(*args, **kwargs)
        
    def created(self):
        return self.created_at.strftime('%d.%m.%Y %H:%M')
    
    def updated(self):
        return self.updated_at.strftime('%d.%m.%Y %H:%M')
        
        
class Faculty(BaseModel):
    title = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'faculty'
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        ordering = ['-id']
        
    def __str__(self):
        return self.title
    

class Group(BaseModel):
    title = models.CharField(max_length=3)
    
    class Meta:
        db_table = 'group'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ['-id']
        
    def __str__(self):
        return self.title
    

class Scholarship(BaseModel):
    title = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'scholarship'
        verbose_name = 'Scholarship'
        verbose_name_plural = 'Scholarships'
        ordering = ['-id']
        
    def __str__(self):
        return self.title

        
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    student_id = models.CharField(max_length=255, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fullname()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        super().save(*args, **kwargs)
        
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    def created(self):
        return self.created_at.strftime('%d.%m.%Y %H:%M')
    
    def updated(self):
        return self.updated_at.strftime('%d.%m.%Y %H:%M')
    
    
    
class Lesson(BaseModel):
    title = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'lesson'
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ['-id']
        
    def __str__(self):
        return self.title
    
    
class Semester(BaseModel):
    title = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'semester'
        verbose_name = 'Semester'
        verbose_name_plural = 'Semesters'
        ordering = ['-id']
        
    def __str__(self):
        return self.title
    
    
class Marks(models.Model):
    class MarkType(models.TextChoices):
        HASAP = 'hasap', 'Hasap'
        SYNAG = 'synag', 'Synag'
        
    class Mark(models.TextChoices):
        HASAP = 'hasap', 'Hasap'
        HASAP_DAL = 'hasap_dal', 'Hasap dal'
        FIVE = '5', '5'
        FOUR = '4', '4'
        THREE = '3', '3'
        TWO = '2', '2'
        
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    mark_type = models.CharField(max_length=5, choices=MarkType.choices, default=MarkType.HASAP)
    mark = models.CharField(max_length=10, choices=Mark.choices, default=Mark.HASAP)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'marks'
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'
        ordering = ['-id']
        
    def __str__(self):
        return f"{self.student.fullname()} - {self.lesson.title} - {self.semester.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(uuid.uuid4()))
        super().save(*args, **kwargs)
    
    def created(self):
        return self.created_at.strftime('%d.%m.%Y %H:%M')
    
    def updated(self):
        return self.updated_at.strftime('%d.%m.%Y %H:%M')