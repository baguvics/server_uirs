from .models import Student, Teacher
from django.forms import ModelForm, TextInput, Textarea


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя студента',
            }),
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["name"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя преподавателя',
            }),
        }
