from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


class AdminSignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','password']


# class LecturerSignUpForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','email','password']


class CourseForm(forms.ModelForm):
   
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'course_type', 'credit_hours', 'contact_hours']


class ProfessorForm(forms.ModelForm):
    
    class Meta:
        model = Lecturer
        fields = ['lecturer_id', 'first_name','last_name','email', 'working_hours','available_hours']


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['classroom_id', 'classroom_name', 'classroom_type']


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = '__all__'

class ClassCourseForm(forms.ModelForm):
    class Meta:
        model = ClassCourse
        fields = '__all__'

class SectionClassroomForm(forms.ModelForm):
    class Meta:
        model = SectionClassroom
        fields = ['class_id', 'classroom_id']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_id', 'activity_type', 'class_id', 'classroom_id', 'course_id', 'lecturer_id', 'day',
                  'start_time', 'end_time']
