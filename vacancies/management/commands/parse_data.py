from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from vacancies.models import Vacancy, Company, Specialty

from data import specialties, companies, jobs



class Command(BaseCommand):
    help = 'Parse data file'

    def handle(self, *args, **options):

        id = 0

        for specialty in specialties:
            Specialty.objects.get_or_create(
                code=specialty['code'],
                title=specialty['title'])


        for company in companies:
            id += 1
            Company.objects.get_or_create(
                    id=company['id'],
                    title=company['title'],
                    # logo=company['logo'],
                    employee_count=company['employee_count'],
                    location=company['location'],
                    description=company['description'],
                    owner=User.objects.get(id=id)
                )

        for job in jobs:

            specialty = Specialty.objects.get(code=job['specialty'])
            company = Company.objects.get(id=job['company'])
            Vacancy.objects.get_or_create(
                    id=job['id'],
                    title=job['title'],
                    specialty = specialty,
                    company = company,
                    skills = job['skills'],
                    description = job['description'],
                    salary_min = job['salary_from'],
                    salary_max = job['salary_to'],
                    published_at = job['posted'],
                )
