from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.http import HttpResponse

from vacancies.models import Vacancy, Company, Specialty


class MainView(View):

    def get(self, request):

        specialisations = []

        for specialisation in Specialty.objects.all():
            specialisations.append(
                {'specialisation': specialisation.title,
                 'code': specialisation.code,
                 'vacancy_count': len(Vacancy.objects.filter(
                     specialty=specialisation))}
            )
        companies = []

        for company in Company.objects.all():
            companies.append(
                {'title': company.title,
                 'logo': company.logo,
                 'id': company.id,
                 'vacancy_count': len(Vacancy.objects.filter(company=company))}
            )
        return render(request, 'index.html', {
            'specialisations': specialisations,
            'companies': companies})


class VacanciesView(ListView):
    model = Vacancy


class VacancyView(DetailView):
    model = Vacancy


class VacancyBySpecialisationView(View):

    def get(self, request, specialisation):
        vacancy = Vacancy.objects.filter(specialty__code=specialisation)
        specialisation = Specialty.objects.get(code=specialisation).title
        return render(request, 'vacancies/vacancy_list.html',
                      {'object_list': vacancy,
                       'specialisation': specialisation})


class CompanyView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.filter(
            company_id=context['object'].id)
        return context


class CompaniesView(ListView):
    model = Company


def page_not_found(request, exception):
    return HttpResponse('Нету такой страницы!')


def server_error(exception):
    return HttpResponse('Что-то сломалось, но мы обязательно починим!')
