import datetime
from users.models import Student, Mentor, Language, Courses

language1 = Language(name='Python',month_to_learn=6)
language1.save()
language2 = Language(name='Java Script',month_to_learn=6)
language2.save()
language3 = Language(name='UX-UI',month_to_learn=2)
language3.save()

student1 = Student(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',
                   work_study_place='School №13', has_own_notebook=True, preferred_os='windows')
student1.save()
student2 = Student(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888',
                   work_study_place='TV', has_own_notebook=True, preferred_os='mac')
student2.save()
student3 = Student(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312',
                   work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='False')
student3.save()

mentor1 = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454',
                                main_work=None,
                                experience=datetime.date(year=2021, month=10, day=23))

mentor2 = Mentor.objects.create(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876',
                                main_work='University of Fort Collins',
                                experience=datetime.date(year=2010, month=9, day=18))

course1 = Courses.objects.create(name='Python-21', mentor=mentor2, student=student1,language='Python',date_started='2022-01-25')
course2 = Courses.objects.create(name='Python-21', mentor=mentor1, student=student2, language='Python',date_started='2022-05-18')

course3 = Courses.objects.create(name='UXUI design-43', mentor=mentor1, student=student3,language='UXUI', date_started='2022-02-05')
