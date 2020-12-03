from django.db.models import Count
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from vacancies.forms import SignupForm, LoginForm
from vacancies.models import Vacancy, Company, Specialty


class MainView(View):

    def get(self, request):

        specialisations = Specialty.objects\
            .values('title', 'code')\
            .annotate(vacancy_count=Count('vacancy'))
        companies = Company.objects\
            .values('title', 'logo', 'id',)\
            .annotate(vacancy_count=Count('vacancy'))

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


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    authentication_form = LoginForm


class MyLogoutView(LogoutView):
     pass


class SignupView(CreateView):
     form_class = SignupForm
     success_url = '/login'
     template_name = 'register.html'

class MyCompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = ['title',  'employee_count', 'location', 'description', 'logo']

    def get_object(self):
        try:
            mycompany = Company.objects.get(owner = self.request.user)
            return mycompany
        except:
            redirect('mycompany_create')


class MyCompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = ['title',  'employee_count', 'location', 'description', 'logo', ]
    def form_valid(self, form):
        company = form.save(commit=False)
        company.owner = self.request.user
        company.save()
        # return super(MyCompanyCreateView, self).form_valid(form)
        # return redirect(self.get_success_url())


# class MyCompanyView(LoginRequiredMixin, View):
#
#     def get(self, request, create=None):
#         company = Company.objects.filter(owner=request.user)
#         if company.exists() or create:
#             form = CompanyEditForm(instance=company.first())
#             return render(request, 'company-edit.html',{'form': form})
#         else:
#             return render(request, 'company-create.html',{})
#
#     def post(self, request, create=None):
#         form = CompanyEditForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             company, created = Company.objects.update_or_create(
#             owner=request.user,
#             defaults={ 'title': data['title'],
#             'location': data['location'],
#             'description': data['description'],
#             'employee_count': data['employee_count'],
#                        'logo': request.FILES['logo']}
#         )
#         return redirect('mycompany')


# class MyVacanciesView(LoginRequiredMixin, View):
#
#     def get(self, request):
#         myvacancies = Vacancy.objects.filter(company__owner=request.user)
#         return render(request, 'my-vacancy-list.html',{'myvacancies': myvacancies})

# class MyVacancyView(LoginRequiredMixin, View):
#
#     def get(self, request, vacancy_id):
#         vacancy = Vacancy.objects.get(id=vacancy_id)
#         form = VacancyEditForm(instance=vacancy)
#         return render(request, 'my-vacancy-edit.html',{'form': form})
#
#     def post(self, request, vacancy_id):
#         form = VacancyEditForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             vacancy = Vacancy.objects.update(data)
#         return redirect(request.path)

class MyVacancyView(DetailView):
    model = Vacancy

class MyVacancyUpdateView(UpdateView):
    model = Vacancy
    fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']

def page_not_found(request, exception):
    return HttpResponse('Нету такой страницы!')


def server_error(exception):
    return HttpResponse('Что-то сломалось, но мы обязательно починим!')
