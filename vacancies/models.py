from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from phonenumber_field.modelfields import PhoneNumberField
from tinymce import HTMLField




class Company(models.Model):
    title = models.CharField(max_length=64, verbose_name=u"Название компании")
    location = models.CharField(max_length=64, verbose_name=u"География")
    logo = models.ImageField(upload_to=settings.MEDIA_COMPANY_IMAGE_DIR, verbose_name=u"Логотип")
    description = models.TextField(verbose_name=u"Информация о компании")
    employee_count = models.IntegerField(verbose_name=u"Количество человек в компании")
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.TextField()
    picture = models.ImageField(upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=64, verbose_name=u"Название вакансии")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name=u"Специализация")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    skills = models.CharField(max_length=64, verbose_name=u"Требуемые навыки")
    description = HTMLField('Content')
    salary_min = models.FloatField(verbose_name=u"Зарплата от")
    salary_max = models.FloatField(verbose_name=u"Зарплата до")
    published_at = models.DateTimeField(auto_now_add=True)


class VacancyApplication(models.Model):
    written_username = models.CharField(max_length=64, verbose_name=u"Имя")
    written_phone = PhoneNumberField(verbose_name=u"Телефон")
    written_cover_letter = models.TextField(verbose_name=u"Сопроводительное письмо")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

class Status(models.Model):
    status = models.CharField(max_length=64, verbose_name=u"Статус")

    def __str__(self):
        return self.status


class  Grade(models.Model):
    grade = models.CharField(max_length=64, verbose_name=u"Квалификация")

    def __str__(self):
        return self.grade


class Resume(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name=u"Статус")
    salary = models.FloatField(verbose_name=u"Ожидаемое вознаграждение")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name=u"Специализация")
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name=u"Квалификация")
    education = HTMLField(u'Образование')
    experience = HTMLField(u'Опыт работы')
    portfolio = models.CharField(max_length=64, verbose_name=u"Ссылка на портфолио")
