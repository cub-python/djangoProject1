from django.db import models
from doctors.models import Doctors

# Create your models here.
class Doctors(models.Model):
    title = models.CharField(max_length=250)
    position = models.CharField(max_length=35)
    education = models.TextField(blank=True)
    speciality = models.CharField(max_length=25)
    experience = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title   #выводит в консоль записи


'''
from doctors.models import Doctors
>>> Doctors(title='Василиса Симонова', position='Главный врач', education='Томский медицинский институт', speciality='Кардиолог') 
<Doctors: Василиса Симонова>
>>> doc1 = _
>>> doc1
<Doctors: Василиса Симонова>
>>> doc1.save()
>>> doc1
<Doctors: Василиса Симонова>
>>> doc1.id
1
>>> from doctors.models import connection
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ImportError: cannot import name 'connection' from 'doctors.models' (/home/jka/djangoProject/medicalCenter/doctors/models.py)
>>> from django.db import connection
>>> connection.queries
[{'sql': 'INSERT INTO "doctors_doctors" ("title", "position", "education", "speciality", "experience", "photo", "time_create", "time_update", "is_published") VALUES (\'Василиса Симонова\', \'Главный врач\', \'Томский медицинский институт\', \'Кардиолог\', 0, \'\', \'2023-02-12 12:05:47.028145\', \'2023-02-12 12:05:47.028196\', 1) RETURNING "doctors_doctors"."id"', 'time': '0.001'}]
>>> doc2 = (title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмен', speciality='Кардиолог') 
[1]+  Остановлен    ./manage.py shell
(djangoProject1) jka@jka-linux:~/djangoProject/medicalCenter$ python manage.py shell
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> doc2 = (title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмен', speciality='Кардиолог') 
  File "<console>", line 1
    doc2 = (title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмен', speciality='Кардиолог') 
            ^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>>   doc2 = (title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмента', speciality='менеджер') 
  File "<console>", line 1
    doc2 = (title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмента', speciality='менеджер') 
IndentationError: unexpected indent
>>> doc2
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'doc2' is not defined
>>>   doc2 = Doctors(title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмента', speciality='менеджер') 
  File "<console>", line 1
    doc2 = Doctors(title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмента', speciality='менеджер') 
IndentationError: unexpected indent
>>> doc2 = Doctors(title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмента', speciality='менеджер') 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Doctors' is not defined
>>> from doctors.models import Doctors
>>> doc2 = Doctors(title='Анастасия Комарова', position='адмнистратор', education='Институт менеджмента', speciality='менеджер') 
>>> doc2
<Doctors: Анастасия Комарова>
>>> doc2.id
>>> doc2.save()
>>> doc2.id
2
>>> Doctors.objects
<django.db.models.manager.Manager object at 0x7f609e51e800>
>>> doc3 = Doctors.objects.create(title='Станислав Демин', education='MCУ', speciality='Стоматолог') 
>>> doc3
<Doctors: Станислав Демин>
>>> doc3.save()
>>> Doctors.objects.all()
<QuerySet [<Doctors: Василиса Симонова>, <Doctors: Анастасия Комарова>, <Doctors: Станислав Демин>]>
>>> person = _
>>> person[1]
<Doctors: Анастасия Комарова>
>>> person[0]
<Doctors: Василиса Симонова>
>>> len(person)
3
>>> for personi in person:
...     print(person.title)
...     print(personi.title)
... for personi in person:
  File "<console>", line 4
    for personi in person:
    ^^^
SyntaxError: invalid syntax
>>> for personi in person:
...             print(personi.title)
... for personi in person:
  File "<console>", line 3
    for personi in person:
    ^^^
SyntaxError: invalid syntax
>>> Doctors.objects.all()
<QuerySet [<Doctors: Василиса Симонова>, <Doctors: Анастасия Комарова>, <Doctors: Станислав Демин>]>
>>> w = _
>>> w[0]
<Doctors: Василиса Симонова>
>>> len(w)
3
>>> Doctors.objects.all()
<QuerySet [<Doctors: Василиса Симонова>, <Doctors: Анастасия Комарова>, <Doctors: Станислав Демин>]>
>>> w = _
>>> len(w)
3
>>> w.all()
<QuerySet [<Doctors: Василиса Симонова>, <Doctors: Анастасия Комарова>, <Doctors: Станислав Демин>]>
>>> for wi in w:
...     print(wi.title)
... 
Василиса Симонова
Анастасия Комарова
Станислав Демин
Doctors.objects.filter(title='Василиса Симонова')
<QuerySet [<Doctors: Василиса Симонова>]>
>>> from django.db import connection
>>> connection.queries
[{'sql': 'INSERT INTO "doctors_doctors" ("title", "position", "education", "speciality", "experience", "photo", "time_create", "time_update", "is_published") VALUES (\'Анастасия Комарова\', \'адмнистратор\', \'Институт менеджмента\', \'менеджер\', 0, \'\', \'2023-02-12 13:17:40.934236\', \'2023-02-12 13:17:40.934294\', 1) RETURNING "doctors_doctors"."id"', 'time': '0.002'}, {'sql': 'INSERT INTO "doctors_doctors" ("title", "position", "education", "speciality", "experience", "photo", "time_create", "time_update", "is_published") VALUES (\'Станислав Демин\', \'\', \'MCУ\', \'Стоматолог\', 0, \'\', \'2023-02-12 15:06:55.700543\', \'2023-02-12 15:06:55.701500\', 1) RETURNING "doctors_doctors"."id"', 'time': '0.002'}, {'sql': 'UPDATE "doctors_doctors" SET "title" = \'Станислав Демин\', "position" = \'\', "education" = \'MCУ\', "speciality" = \'Стоматолог\', "experience" = 0, "photo" = \'\', "time_create" = \'2023-02-12 15:07:14.428361\', "time_update" = \'2023-02-12 15:07:14.428371\', "is_published" = 1 WHERE "doctors_doctors"."id" = 3', 'time': '0.007'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors" LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors" LIMIT 1 OFFSET 1', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors" LIMIT 1', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors"', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors" LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors" LIMIT 1', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors"', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors" LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors"', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors" LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "doctors_doctors"."id", "doctors_doctors"."title", "doctors_doctors"."position", "doctors_doctors"."education", "doctors_doctors"."speciality", "doctors_doctors"."experience", "doctors_doctors"."photo", "doctors_doctors"."time_create", "doctors_doctors"."time_update", "doctors_doctors"."is_published" FROM "doctors_doctors" WHERE "doctors_doctors"."title" = \'Василиса Симонова\' LIMIT 21', 'time': '0.000'}]
>>> Doctors.objects.filter(pk__gte=2)
<QuerySet [<Doctors: Анастасия Комарова>, <Doctors: Станислав Демин>]>


'''