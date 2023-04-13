import django.db.models.deletion
from django.db import models


class Teacher(models.Model):
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20, blank=True, null=True)
    patronymic = models.CharField("Отчество", max_length=20, blank=True, null=True)
    position = models.CharField('Должность', max_length=50)

    def __str__(self):
        return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.patronymic)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Student(models.Model):
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20, blank=True, null=True)
    patronymic = models.CharField("Отчество", max_length=20, blank=True, null=True)
    group = models.ForeignKey('Group', on_delete=django.db.models.deletion.SET_NULL, null=True)
    teacher = models.ForeignKey("Teacher", on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)
    report_status = models.BooleanField('Отчет сдан/несдан', null=True, default=False)

    def as_json(self):
        return dict(

            name=self.name,
            surname=self.surname,
            patronymic=self.patronymic,
            group=self.group,
            teacher=self.teacher,
            report_status=self.report_status
        )

    def __str__(self):
        return str(self.surname) + ' ' + str(self.name) + ' ' + str(self.patronymic)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Group(models.Model):
    number = models.CharField("Номер группы", max_length=20)
    department = models.ForeignKey('Department', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Department(models.Model):
    name = models.CharField("Название направления", max_length=50)
    director = models.ForeignKey('Teacher', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Themes(models.Model):
    title = models.CharField("Тема", max_length=50)
    student = models.ForeignKey('Student', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)
    teacher = models.ForeignKey('Teacher', related_name='teacher_theme_set',
                                on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)
    consultant = models.ForeignKey('Teacher', related_name='consultant_theme_set',
                                   on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)
