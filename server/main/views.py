from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Teacher, Group, Department, Themes
from .forms import StudentForm, TeacherForm
from .generateDocument import Report
from django.http import HttpResponse
from .serializers import StudentSerializer
from rest_framework import generics
from django.forms.models import model_to_dict
import json
from django.core import serializers


def index(request):
    return render(request, 'main/index.html')


def ajax_datalist(request):
    return render(request, 'main/ajax-datalist.html')


class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''
class group(APIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request):
        print(request.POST)
        print(request.GET)
        group_number = request.POST['group']
        group_id = Group.objects.get(number=group_number)
        group_students = Student.objects.filter(group=group_id)

        results = [student for student in group_students]
        # HttpResponse(json.dumps(group_students), content_type="application/json")
        return Response(group_students, content_type="application/json")


'''


def goals_to_array(request) -> []:
    goals1, goals2 = [], []
    for goal in request.POST:
        if goal[:5] == 'goal1':
            goals1.append(request.POST[goal])
        elif goal[:5] == 'goal2':
            goals2.append(request.POST[goal])
    total_goals = [goals1, goals2]
    return total_goals


def group(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.GET)
        group_number = request.POST['group']
        group_id = Group.objects.get(number=group_number)
        group_students = Student.objects.filter(group=group_id)

        results = [student for student in group_students]
        people = serializers.serialize("json", group_students)
        return HttpResponse(people, content_type="application/json")
    else:
        return HttpResponse((Student.objects.all()))


def about(request):
    return render(request, 'main/about-us.html')


def testingajax(request):
    students_list = Student.objects.all()
    return render(request, 'main/testingajax.html')


def indexnew(request):
    students_list = Student.objects.all()
    teachers_list = Teacher.objects.all()
    groups_list = Group.objects.all()

    error = ''
    # lflflfllf
    if request.method == "POST":
        print(request.POST)
        total_goals = goals_to_array(request)
        teacher_name = str(request.POST["teacher_name"])
        assistant_name = str(request.POST["consultant_name"])
        student_name = str(request.POST["student_name"])
        group_number = str(request.POST["group_number"])
        title = str(request.POST["title_name"])
        students_group = Group.objects.get(number=group_number)
        department = Department.objects.get(name=students_group.department)
        main_teacher_name = department.director.surname + ' ' + \
                            department.director.name[0] + '. ' + department.director.patronymic[0] + '.'
        generated_report = Report(student_name=student_name, teacher_name=teacher_name, total_goals=total_goals,
                                  group_number=group_number, main_teacher_name=main_teacher_name, title=title, assistant_name=assistant_name)
        generated_report.generate_report()

        return redirect('/indexnew')
    else:
        error = 'Форма была неверной'
    form = StudentForm
    context = {
        'form': form,
        "error": error,
        'students_list': students_list,
        'teachers_list': teachers_list,
        'groups_list': groups_list,

    }

    return render(request, 'main/indexnew.html', context)


def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm
    context = {
        'form': form,
        "error": error,
    }
    return render(request, 'main/create.html', context)
