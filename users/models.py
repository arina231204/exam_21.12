from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=20)
    month_to_learn = models.IntegerField()

    def replace_language(self):
        return self.name.title()

    def __str__(self):
        return self.name

class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)

    class Meta:
        abstract = True

    def replace_phone(self):
        if self.phone_number[0] == '0':
            phone_number = '+996' + self.phone_number[1:]
            return phone_number

    def __str__(self):
        return self.name

class Student(AbstractPerson):
    choices_pr = (('mac', 'MacOS'),('windows', 'Windows'),('linux', 'Linux'))
    work_study_place = models.CharField(max_length=20, blank = True,null = True)
    has_own_notebook =  models.BooleanField(default=False)
    preferred_os = models.CharField(max_length=20, choices = choices_pr)

class Mentor(AbstractPerson):
    student = models.ManyToManyField(Student, related_name='students', through='Courses')
    main_work = models.CharField(max_length=50, blank = True,null = True)
    experience = models.DateField()

class Courses(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    date_started = models.DateField()

    def get_end_date(self):
        finish_date = self.date_started.month + self.language.month_to_learn
        return finish_date


    def __str__(self):
        return f'{self.mentor.main_work} - {self.student.name}'

