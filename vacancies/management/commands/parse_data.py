from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from vacancies.models import Vacancy, Company, Specialty

from data import specialties, companies, jobs


class Command(BaseCommand):

    def handle(self, *args, **options):

        _id = 0

        for specialty in specialties:
            Specialty.objects.get_or_create(
                code=specialty['code'],
                title=specialty['title'])

        for company in companies:
            _id += 1
            Company.objects.get_or_create(
                    id=company['id'],
                    title=company['title'],
                    employee_count=company['employee_count'],
                    location=company['location'],
                    description=company['description'],
                    owner=User.objects.get(id=_id),
                )

        for job in jobs:

            specialty = Specialty.objects.get(code=job['specialty'])
            company = Company.objects.get(id=job['company'])
            Vacancy.objects.get_or_create(
                    id=job['id'],
                    title=job['title'],
                    specialty=specialty,
                    company=company,
                    skills=job['skills'],
                    description=job['description'],
                    salary_min=job['salary_from'],
                    salary_max=job['salary_to'],
                    published_at=job['posted'],
                )
