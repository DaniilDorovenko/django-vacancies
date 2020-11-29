from django.db import models


class Company(models.Model):
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.FilePathField()
    description = models.TextField()
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.TextField()
    picture = models.FilePathField()


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    skills = models.CharField(max_length=64)
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateTimeField()


# parser starts here

# from data import specialties, companies, jobs

# for specialty in specialties:
#     new_speciality = Specialty(
#     code=specialty['code'],
#     title=specialty['title'])
#     new_speciality.save()
#
# for company in companies:
#     new_company = Company(
#         id=company['id'],
#         title=company['title'],
#         logo=company['logo'],
#         employee_count=company['employee_count'],
#         location=company['location'],
#         description=company['description'],
#     )
#     new_company.save()

# for job in jobs:
#     specialty = Specialty.objects.get(code=job['specialty'])
#     company = Company.objects.get(id=job['company'])
#     new_job = Vacancy(
#         id=job['id'],
#         title=job['title'],
#         specialty = specialty,
#         company = company,
#         skills = job['skills'],
#         description = job['description'],
#         salary_min = job['salary_from'],
#         salary_max = job['salary_to'],
#         published_at = job['posted'],
#     )
#     new_job.save()
